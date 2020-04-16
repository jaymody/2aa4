JFLAGS = -g
JCLASS = -cp "src:.:junit-4.5.jar"
JC = javac
JVM = java

.PHONY: all
all:
	find . -name '*.class' -exec rm -f {} \;
	$(JC) $(JCLASS) $(JFLAGS) ./src/TestSeq1D.java
	$(JVM) $(JCLASS) org.junit.runner.JUnitCore src.TestSeq1D
