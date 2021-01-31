package main.groovy.groovuinoml.dsl;

import java.util.*;

import groovy.lang.Binding;
import arduinoml.kernel.App;
import arduinoml.kernel.behavioral.Action;
import arduinoml.kernel.behavioral.BeforeState;
import arduinoml.kernel.behavioral.State;
import arduinoml.kernel.behavioral.Transition;
import arduinoml.kernel.behavioral.Condition;
import arduinoml.kernel.generator.ToWiring;
import arduinoml.kernel.generator.Visitor;
import arduinoml.kernel.structural.Actuator;
import arduinoml.kernel.structural.Brick;
import arduinoml.kernel.structural.SIGNAL;
import arduinoml.kernel.structural.BEEP;
import arduinoml.kernel.structural.Sensor;

public class GroovuinoMLModel {
	private List<Brick> bricks;
	private List<State> states;
	private State initialState;
	
	private Binding binding;
	
	public GroovuinoMLModel(Binding binding) {
		this.bricks = new ArrayList<Brick>();
		this.states = new ArrayList<State>();
		this.binding = binding;
	}
	
	public void createSensor(String name, Integer pinNumber) {
		Sensor sensor = new Sensor();
		sensor.setName(name);
		sensor.setPin(pinNumber);
		this.bricks.add(sensor);
		this.binding.setVariable(name, sensor);
//		System.out.println("> sensor " + name + " on pin " + pinNumber);
	}
	
	public void createActuator(String name, Integer pinNumber) {
		Actuator actuator = new Actuator();
		actuator.setName(name);
		actuator.setPin(pinNumber);
		this.bricks.add(actuator);
		this.binding.setVariable(name, actuator);
	}
	
	public void createState(String name, List<Action> actions) {
		State state = new State();
		state.setName(name);
		state.setActions(actions);
		this.states.add(state);
		this.binding.setVariable(name, state);
	}
	
	public void createTransition(State from, State to, boolean isAND, List<Condition> conditions) {
		Transition transition = new Transition();
		transition.setNext(to);
		transition.setIsLogicalAND(isAND);
		transition.setConditions(conditions);
		from.setTransition(transition);
	}

	public void createBeforeState(State state, Actuator actuator, List<BEEP> beeps) {
		BeforeState beforeState = new BeforeState();
		beforeState.setActuator(actuator);
		beforeState.setBeeps(beeps);
		state.setBeforeState(beforeState);
	}
	
	public void setInitialState(State state) {
		this.initialState = state;
	}
	
	@SuppressWarnings("rawtypes")
	public Object generateCode(String appName) {
		App app = new App();
		app.setName(appName);
		app.setBricks(this.bricks);
		app.setStates(this.states);
		app.setInitial(this.initialState);
		Visitor codeGenerator = new ToWiring();
		app.accept(codeGenerator);
		
		return codeGenerator.getResult();
	}
}
