package arduinoml.kernel;

import arduinoml.kernel.behavioral.State;
import arduinoml.kernel.generator.Visitable;
import arduinoml.kernel.generator.Visitor;
import arduinoml.kernel.structural.Brick;

import java.util.ArrayList;
import java.util.List;

public class App implements NamedElement, Visitable {

	private String name;
	private List<Brick> bricks = new ArrayList<Brick>();
	private List<State> states = new ArrayList<State>();
	private State initial;

	@Override
	public String getName() {
		return name;
	}

	@Override
	public void setName(String name) {
		this.name = name;
	}

	public List<Brick> getBricks() {
		return bricks;
	}

	public void setBricks(List<Brick> bricks) {
		this.bricks = bricks;
	}

	public List<State> getStates() {
		return states;
	}

	public void setStates(List<State> states) {
		this.states = states;
	}

	public State getInitial() {
		return initial;
	}

	public void setInitial(State initial) {
		this.initial = initial;
	}

	@Override
	public void accept(Visitor visitor) {
		visitor.visit(this);
	}
}
