package arduinoml.kernel.behavioral;

import arduinoml.kernel.generator.Visitable;
import arduinoml.kernel.generator.Visitor;
import arduinoml.kernel.structural.*;

public class Condition implements Visitable {

	private Sensor sensor;
	private SIGNAL value;

	public Sensor getSensor() {
		return sensor;
	}

	public void setSensor(Sensor sensor) {
		this.sensor = sensor;
	}

	public SIGNAL getValue() {
		return value;
	}

	public void setValue(SIGNAL value) {
		this.value = value;
	}

	@Override
	public void accept(Visitor visitor) {
		visitor.visit(this);
	}
}
