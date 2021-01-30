package arduinoml.kernel.behavioral;

import arduinoml.kernel.generator.Visitable;
import arduinoml.kernel.generator.Visitor;
import arduinoml.kernel.structural.Actuator;
import arduinoml.kernel.structural.BEEP;

import java.util.ArrayList;
import java.util.List;

public class BeforeState implements Visitable {

	private List<BEEP> beeps = new ArrayList<BEEP>();
	private Actuator actuator;


	public List<BEEP> getBeeps() {
		return beeps;
	}

	public void setBeeps(List<BEEP> beeps) {
		this.beeps = beeps;
	}

	public Actuator getActuator() {
		return actuator;
	}

	public void setActuator(Actuator actuator) {
		this.actuator = actuator;
	}

	@Override
	public void accept(Visitor visitor) {
		visitor.visit(this);
	}
}