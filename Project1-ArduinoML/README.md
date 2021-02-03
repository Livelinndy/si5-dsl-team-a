## Compile JVM kernel
*internal and external DSL are using the same kernel (compile it once for both implementations)*

Into `Project1-ArduinoML/kernel-jvm` folder run this command `mvn clean install`

***
## Run Internal DSL implemented with Groovy

Into `Project1-ArduinoML/internal-DSL-groovy` run the following command to build an executable jar `mvn clean compile assembly:single`.

To execute a script run this command `java -jar target\dsl-groovy-1.0-jar-with-dependencies.jar scripts\<script_name>.groovy` into the same directory.

***
## Run External DSL implemented with AntLR

Into `Project1-Arduino/external-DSL-antlr` run the following command `mvn clean package` and `mvn exec:java -Dexec.args="src/main/resources/<script_name>.arduinoml` to try the scripts.

***