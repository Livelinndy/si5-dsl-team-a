## Compile JVM kernel
*internal and external DSL are using the same kernel (compile it once for both implementations)*

In the `kernel-jvm` directory, run `mvn clean install`

***
## Run Internal DSL implemented with Groovy

In the `internal-DSL-groovy` directory, run `mvn clean compile assembly:single` to build an executable jar.

To execute a script, run `java -jar target\dsl-groovy-1.0-jar-with-dependencies.jar scripts\<script_name>.groovy` in the same directory.

***
## Run External DSL implemented with AntLR

In the `external-DSL-antlr` directory, run `mvn clean package` to compile the code.

To execute a script, run `mvn exec:java -Dexec.args="src/main/resources/<script_name>.arduinoml` in the same directory.

***
