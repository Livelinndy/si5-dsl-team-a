package io.github.mosser.arduinoml.kernel.samples;

import arduinoml.kernel.App;
import arduinoml.kernel.behavioral.*;
import arduinoml.kernel.generator.ToWiring;
import arduinoml.kernel.generator.Visitor;
import arduinoml.kernel.structural.*;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class Switch {

	public static void main(String[] args) {

		// Declaring elementary bricks
		Sensor button = new Sensor();
		button.setName("button");
		button.setPin(9);

		Actuator led = new Actuator();
		led.setName("LED");
		led.setPin(12);

		Actuator buzzer = new Actuator();
		buzzer.setName("BUZZER");
		buzzer.setPin(2);

		
		// Declaring states
		State on = new State();
		on.setName("on");

		State off = new State();
		off.setName("off");

		// Creating actions
		Action switchTheLightOn = new Action();
		switchTheLightOn.setActuator(led);
		switchTheLightOn.setValue(SIGNAL.HIGH);

		Action switchTheLightOff = new Action();
		switchTheLightOff.setActuator(led);
		switchTheLightOff.setValue(SIGNAL.LOW);

		// Binding actions to states
		on.setActions(Arrays.asList(switchTheLightOn));
		off.setActions(Arrays.asList(switchTheLightOff));

		// Creating beforeState
		BeforeState beforeState = new BeforeState();
		List<BEEP> beeps = new ArrayList<BEEP>();
		beeps.add(BEEP.SHORTBEEP);
		beeps.add(BEEP.SHORTBEEP);
		beeps.add(BEEP.SHORTBEEP);
		beforeState.setBeeps(beeps);
		beforeState.setActuator(buzzer);

		// Creating transitions
		Transition on2off = new Transition();
		on2off.setNext(off);
		Condition conditionOne = new Condition();
		conditionOne.setSensor(button);
		conditionOne.setValue(SIGNAL.HIGH);
		List<Condition> conditionListOne = new ArrayList<Condition>();
		conditionListOne.add(conditionOne);
		on2off.setConditions(conditionListOne);


		Transition off2on = new Transition();
		off2on.setNext(on);
		Condition condition = new Condition();
		condition.setSensor(button);
		condition.setValue(SIGNAL.HIGH);
		List<Condition> conditionList = new ArrayList<Condition>();
		conditionList.add(condition);
		off2on.setConditions(conditionList);

		// Binding transitions to states
		on.setTransition(on2off);
		off.setTransition(off2on);

		// Building the App
		App theSwitch = new App();
		theSwitch.setName("Switch!");
		theSwitch.setBricks(Arrays.asList(button, led ));
		theSwitch.setStates(Arrays.asList(on, off));
		theSwitch.setInitial(off);

		// Generating Code
		Visitor codeGenerator = new ToWiring();
		theSwitch.accept(codeGenerator);

		// Printing the generated code on the console
		System.out.println(codeGenerator.getResult());
	}

}
