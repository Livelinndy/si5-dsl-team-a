package arduinoml.externals.antlr;

import arduinoml.externals.antlr.grammar.*;


import arduinoml.kernel.App;
import arduinoml.kernel.behavioral.Action;
import arduinoml.kernel.behavioral.Terminal;
import arduinoml.kernel.behavioral.Condition;
import arduinoml.kernel.behavioral.State;
import arduinoml.kernel.behavioral.Transition;
import arduinoml.kernel.structural.Actuator;
import arduinoml.kernel.structural.SIGNAL;
import arduinoml.kernel.structural.Sensor;

import java.util.HashMap;
import java.util.Map;

public class ModelBuilder extends ArduinomlBaseListener {

    /********************
     ** Business Logic **
     ********************/

    private App theApp = null;
    private boolean built = false;

    public App retrieve() {
        if (built) { return theApp; }
        throw new RuntimeException("Cannot retrieve a model that was not created!");
    }

    /*******************
     ** Symbol tables **
     *******************/

    private Map<String, Sensor>   sensors   = new HashMap<>();
    private Map<String, Actuator> actuators = new HashMap<>();
    private Map<String, State>    states  = new HashMap<>();
    private Map<String, Binding>  bindings  = new HashMap<>();

    private class Binding { // used to support state resolution for transitions
        String to; // name of the next state, as its instance might not have been compiled yet
        Condition condition; //sensor and value
    }

    private State currentState = null;
    private Binding currentBinding = null;
    private Terminal currentTerminal = null;

    /**************************
     ** Listening mechanisms **
     **************************/

    @Override
    public void enterRoot(ArduinomlParser.RootContext ctx) {
        built = false;
        theApp = new App();
    }

    @Override public void exitRoot(ArduinomlParser.RootContext ctx) {
        // Resolving states in transitions
        bindings.forEach((key, binding) ->  {
            Transition t = new Transition();
            // t.setSensor(binding.trigger);
            // t.setValue(binding.value);
            t.setConditions(bindings.condition);
            t.setNext(states.get(binding.to));
            states.get(key).setTransition(t);
        });
        this.built = true;
    }

    @Override
    public void enterDeclaration(ArduinomlParser.DeclarationContext ctx) {
        theApp.setName(ctx.name.getText());
    }

    @Override
    public void enterSensor(ArduinomlParser.SensorContext ctx) {
        Sensor sensor = new Sensor();
        sensor.setName(ctx.location().id.getText());
        sensor.setPin(Integer.parseInt(ctx.location().port.getText()));
        this.theApp.getBricks().add(sensor);
        sensors.put(sensor.getName(), sensor);
    }

    @Override
    public void enterActuator(ArduinomlParser.ActuatorContext ctx) {
        Actuator actuator = new Actuator();
        actuator.setName(ctx.location().id.getText());
        actuator.setPin(Integer.parseInt(ctx.location().port.getText()));
        this.theApp.getBricks().add(actuator);
        actuators.put(actuator.getName(), actuator);
    }

    @Override
    public void enterState(ArduinomlParser.StateContext ctx) {
        State local = new State();
        local.setName(ctx.name.getText());
        this.currentState = local;
        this.states.put(local.getName(), local);
    }

    @Override
    public void exitState(ArduinomlParser.StateContext ctx) {
        this.theApp.getStates().add(this.currentState);
        this.currentState = null;
    }

    @Override
    public void enterAction(ArduinomlParser.ActionContext ctx) {
        Action action = new Action();
        action.setActuator(actuators.get(ctx.receiver.getText()));
        action.setValue(SIGNAL.valueOf(ctx.value.getText()));
        currentState.getActions().add(action);
    }

    @Override
    public void enterTransition(ArduinomlParser.TransitionContext ctx) {
        // Creating a placeholder as the next state might not have been compiled yet.
        Binding toBeResolvedLater = new Binding();
        toBeResolvedLater.to      = ctx.next.getText();
        toBeResolvedLater.condition = new ArrayList<Condition>();

        Condition condition = new Condition();
        condition.setSensor(sensors.get(ctx.trigger.getText()));
        condition.setValue(SIGNAL.valueOf(ctx.value.getText()));
        toBeResolvedLater.condition.add(condition);
        this.currentBinding = toBeResolvedLater;
    }

    @Override
    public void exitTransition(ArduinomlParser.TransitionContext ctx) {
        bindings.put(currentState.getName(), this.currentBinding);
        this.currentBinding = null;
    }

    @Override
    void enterCondition(ArduinomlParser.InitialContext ctx) {
        Condition condition = new Condition();
        condition.setSensor(sensors.get(ctx.trigger.getText()));
        condition.setValue(SIGNAL.valueOf(ctx.value.getText()));
        currentBinding.condition.add(condition);
    }

    // void exitCondition(ArduinomlParser.InitialContext ctx) {}

    @Override
    public void enterInitial(ArduinomlParser.InitialContext ctx) {
        this.theApp.setInitial(this.currentState);
    }

}

