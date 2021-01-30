package arduinoml.kernel.behavioral;

import arduinoml.kernel.generator.Visitable;
import arduinoml.kernel.generator.Visitor;

import java.util.ArrayList;
import java.util.List;

public class Transition implements Visitable {

	private State next;
	private boolean isLogicalAND = true;
	private List<Condition> conditions = new ArrayList<Condition>();

	public State getNext() {
		return next;
	}

	public boolean getIsLogicalAND() { return isLogicalAND;}

	public void setIsLogicalAND(boolean _isAND) {
		isLogicalAND = _isAND;
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
