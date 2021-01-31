package arduinoml.kernel.generator;

import arduinoml.kernel.App;
import arduinoml.kernel.behavioral.*;
import arduinoml.kernel.structural.*;

/**
 * Quick and dirty visitor to support the generation of Wiring code
 */
public class ToWiring extends Visitor<StringBuffer> {
	enum PASS {ONE, TWO}

	public ToWiring() {
		this.result = new StringBuffer();
	}

	private void w(String s) {
		result.append(String.format("%s",s));
	}

	@Override
	public void visit(App app) {
		//first pass, create global vars
		context.put("pass", PASS.ONE);
		w("// Wiring code generated from an ArduinoML model\n");
		w(String.format("// Application name: %s\n", app.getName())+"\n");

		w("long debounce = 200;\n");
		w("\nenum STATE {");
		String sep ="";
		for(State state: app.getStates()){
			w(sep);
			state.accept(this);
			sep=", ";
		}
		w("};\n");
		if (app.getInitial() != null) {
			w("STATE currentState = " + app.getInitial().getName()+";\n");
		}

		for(State state: app.getStates()){
			if(state.getBeforeState() != null){
				w(String.format("boolean enter%s = false;\n", state.getName()));
			}
		}

		for(Brick brick: app.getBricks()){
			brick.accept(this);
		}

		//second pass, setup and loop
		context.put("pass",PASS.TWO);
		w("\nvoid setup(){\n");
		for(Brick brick: app.getBricks()){
			brick.accept(this);
		}
		w("}\n");

		w("void shortBeep(int buzzer) {\n" +
				"    for(int i = 0; i < 10; i++) {\n" +
				"      digitalWrite(buzzer, HIGH);\n" +
				"      delay(1);\n" +
				"      digitalWrite(buzzer, LOW);\n" +
				"      delay(1);\n" +
				"    }\n" +
				"}\n\n");
		w("void longBeep(int buzzer) {\n" +
				"    for(int i = 0; i < 160; i++) {\n" +
				"      digitalWrite(buzzer, HIGH);\n" +
				"      delay(2);\n" +
				"      digitalWrite(buzzer, LOW);\n" +
				"      delay(2);\n" +
				"    }" +
				"}\n\n");

		w("\nvoid loop() {\n" +
			"\tswitch(currentState){\n");
		for(State state: app.getStates()){
			state.accept(this);
		}
		w("\t}\n" +
			"}");
	}

	@Override
	public void visit(Actuator actuator) {
		if(context.get("pass") == PASS.ONE) {
			w("const int "+actuator.getName()+" = "+actuator.getPin()+";\n");
			return;
		}
		if(context.get("pass") == PASS.TWO) {
			w(String.format("  pinMode(%s, OUTPUT); // Actuator\n", actuator.getName()));
			return;
		}
	}

	@Override
	public void visit(Sensor sensor) {
		if(context.get("pass") == PASS.ONE) {
			w(String.format("\nboolean %sBounceGuard = false;\n", sensor.getName()));
			w(String.format("long %sLastDebounceTime = 0;\n", sensor.getName()));
			w("const int "+sensor.getName()+" = "+sensor.getPin()+";\n");
			return;
		}
		if(context.get("pass") == PASS.TWO) {
			w(String.format("  pinMode(%s, INPUT);  // Sensor\n", sensor.getName()));
			return;
		}
	}

	@Override
	public void visit(BeforeState beforeState){
		if(context.get("pass") == PASS.ONE){
			return;
		}
		if(context.get("pass") == PASS.TWO){
			String step = "";
			for(BEEP beep : beforeState.getBeeps()){
				w(String.format("\t\t\t%s\n", step));
				w(String.format("\t\t\tdigitalWrite(%s, HIGH);\n", beforeState.getActuator().getName()));
				if( beep == BEEP.LONGBEEP ){
					w("\t\t\tdelay(1500);\n");
				}
				else if( beep == BEEP.SHORTBEEP ){
					w("\t\t\tdelay(500);\n");
				}
				w(String.format("\t\t\tdigitalWrite(%s, LOW);\n", beforeState.getActuator().getName()));
				step = "delay(500);";
			}
			w("\t\t}\n");
			return;
		}
	}

	@Override
	public void visit(State state) {
		if(context.get("pass") == PASS.ONE){
			w(state.getName());
			return;
		}
		if(context.get("pass") == PASS.TWO) {
			w("\t\tcase " + state.getName() + ":\n");
			BeforeState beforeState = state.getBeforeState();
			if(beforeState != null && beforeState.getBeeps().size() > 0){
				w(String.format("\t\tif( !enter%s ) {\n", state.getName()));
				w(String.format("\t\t\tenter%s = true;\n", state.getName()));
				beforeState.accept(this);
			}
			for (Action action : state.getActions()) {
				action.accept(this);
			}

			if (state.getTransition() != null) {
				state.getTransition().accept(this);
				w("\t\t\tbreak;\n");
			}
			return;
		}

	}

	// @Override
	// public void visit(Condition condition) { }

	@Override
	public void visit(Transition transition) {
		if(context.get("pass") == PASS.ONE) {
			return;
		}
		if(context.get("pass") == PASS.TWO) {
			String sensorName = transition.getConditions().get(0).getSensor().getName();
			w(String.format("\t\t\t%sBounceGuard = millis() - %sLastDebounceTime > debounce;\n",
					sensorName, sensorName));
			w("\t\t\tif( (");
			String sep = "";
			for (Condition condition: transition.getConditions()) {
				w(String.format(
						"%sdigitalRead(%s) == %s", sep,
						condition.getSensor().getName(), condition.getValue()));
				sep = transition.getIsLogicalAND() ? " && " : " || ";
			}
			w(String.format(" ) && %sBounceGuard) {\n", sensorName));
			w(String.format("\t\t\t\t%sLastDebounceTime = millis();\n", sensorName));
			State nextState = transition.getNext();
			w("\t\t\t\tcurrentState = " + nextState.getName() + ";\n");
			if(nextState.getBeforeState() != null){
				w(String.format("\t\t\t\tenter%s = false;\n", nextState.getName()));
			}
			w("\t\t\t}\n");
			return;
		}
	}

	@Override
	public void visit(Action action) {
		if(context.get("pass") == PASS.ONE) {
			return;
		}
		if(context.get("pass") == PASS.TWO) {
			w(String.format("\t\t\tdigitalWrite(%s,%s);\n",action.getActuator().getName(),action.getValue()));
			return;
		}
	}

	@Override
	public void visit(Condition condition) {
		if(context.get("pass") == PASS.ONE) {
			return;
		}
		if(context.get("pass") == PASS.TWO) {
			w(String.format("\t\t\t%s == %s",condition.getSensor().getName(),condition.getValue()));
			return;
		}
	}
}
