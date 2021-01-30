package arduinoml.kernel.behavioral;

import arduinoml.kernel.generator.Visitable;
import arduinoml.kernel.generator.Visitor;
import arduinoml.kernel.structural.*;

public class Transition implements Visitable {

	private State next;
	private List<Condition> conditions = new ArrayList<Condition>();


	public State getNext() {
		return next;
	}

	public void setNext(State next) {
		this.next = next;
	}

	public List<Condition> getConditions() {
		return conditions;
	}

	public void setConditions(List<Condition> conditions) {
		this.conditions = conditions;
	}

	@Override
	public void accept(Visitor visitor) {
		visitor.visit(this);
	}
}
