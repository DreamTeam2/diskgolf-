all: src
	find . -name "*.java" -print | xargs javac -d bin
	jar cvf import.jar bin
run: import.jar
	java -cp import.jar engine.Spracovanie
