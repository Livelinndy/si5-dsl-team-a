package main.groovy.groovuinoml.dsl

import java.util.List;

import arduinoml.kernel.behavioral.Action
import arduinoml.kernel.behavioral.State
import arduinoml.kernel.behavioral.Condition
import arduinoml.kernel.structural.Actuator
import arduinoml.kernel.structural.Sensor
import arduinoml.kernel.structural.SIGNAL
import arduinoml.kernel.structural.BEEP

abstract class GroovuinoMLBasescript extends Script {
	// sensor "name" pin n
	def sensor(String name) {
		[pin: { n -> ((GroovuinoMLBinding)this.getBinding()).getGroovuinoMLModel().createSensor(name, n) },
		onPin: { n -> ((GroovuinoMLBinding)this.getBinding()).getGroovuinoMLModel().createSensor(name, n)}]
	}
	
	// actuator "name" pin n
	def actuator(String name) {
		[pin: { n -> ((GroovuinoMLBinding)this.getBinding()).getGroovuinoMLModel().createActuator(name, n) }]
	}
	
	// state "name" means actuator becomes signal [and actuator becomes signal]*n
	def state(String name) {
		List<Action> actions = new ArrayList<Action>()
		((GroovuinoMLBinding) this.getBinding()).getGroovuinoMLModel().createState(name, actions)
		// recursive closure to allow multiple and statements
		def closure
		closure = { actuator -> 
			[becomes: { signal ->
				Action action = new Action()
				action.setActuator(actuator instanceof String ? (Actuator)((GroovuinoMLBinding)this.getBinding()).getVariable(actuator) : (Actuator)actuator)
				action.setValue(signal instanceof String ? (SIGNAL)((GroovuinoMLBinding)this.getBinding()).getVariable(signal) : (SIGNAL)signal)
				actions.add(action)
				[and: closure]
			}]
		}
		[means: closure]
	}
	
	def before(state) {
		[with: { actuator -> 
			List<BEEP> beeps = new ArrayList<BEEP>()
			((GroovuinoMLBinding) this.getBinding()).getGroovuinoMLModel().createBeforeState(
				state instanceof String ? (State)((GroovuinoMLBinding)this.getBinding()).getVariable(state) : (State)state,
				actuator instanceof String ? (Actuator)((GroovuinoMLBinding)this.getBinding()).getVariable(actuator) : (Actuator)actuator,
				beeps)
			def close
			close = { beep ->
				beeps.add(beep instanceof String ? (BEEP)((GroovuinoMLBinding)this.getBinding()).getVariable(beep) : (BEEP)beep)
				[and: close]
			}
			[make: close]
		}]
	}
	
	// initial state
	def initial(state) {
		((GroovuinoMLBinding) this.getBinding()).getGroovuinoMLModel().setInitialState(state instanceof String ? (State)((GroovuinoMLBinding)this.getBinding()).getVariable(state) : (State)state)
	}
	
	// from state1 to state2 when sensor becomes signal
	def from(state1) {
		[to: { state2 -> 
			boolean isLogicalAND = true;
			State stateOne = state1 instanceof String ? (State)((GroovuinoMLBinding)this.getBinding()).getVariable(state1) : (State)state1
			List<Condition> conditions = new ArrayList<Condition>()
			((GroovuinoMLBinding) this.getBinding()).getGroovuinoMLModel().createTransition(
				stateOne,
				state2 instanceof String ? (State)((GroovuinoMLBinding)this.getBinding()).getVariable(state2) : (State)state2,
				isLogicalAND,
				conditions)
			def closeOR
			def closeAND
			closeAND = { sensor ->
				[becomes: { signal -> 
					stateOne.getTransition().setIsLogicalAND(true);
					Condition condition = new Condition()
					condition.setSensor(sensor instanceof String ? (Sensor)((GroovuinoMLBinding)this.getBinding()).getVariable(sensor) : (Sensor)sensor)
					condition.setValue(signal instanceof String ? (SIGNAL)((GroovuinoMLBinding)this.getBinding()).getVariable(signal) : (SIGNAL)signal)
					conditions.add(condition)
					[and: closeAND, or: closeOR]
				}]
			}
			closeOR = { sensor ->
				[becomes: { signal -> 
					stateOne.getTransition().setIsLogicalAND(false);
					Condition condition = new Condition()
					condition.setSensor(sensor instanceof String ? (Sensor)((GroovuinoMLBinding)this.getBinding()).getVariable(sensor) : (Sensor)sensor)
					condition.setValue(signal instanceof String ? (SIGNAL)((GroovuinoMLBinding)this.getBinding()).getVariable(signal) : (SIGNAL)signal)
					conditions.add(condition)
					[and: closeAND, or: closeOR]
				}]
			}
			[when: closeAND]
		}]
	}

	// export name
	def export(String name) {
		println(((GroovuinoMLBinding) this.getBinding()).getGroovuinoMLModel().generateCode(name).toString())
	}
	
	// disable run method while running
	int count = 0
	abstract void scriptBody()
	def run() {
		if(count == 0) {
			count++
			scriptBody()
		} else {
			println "Run method is disabled"
		}
	}
}
