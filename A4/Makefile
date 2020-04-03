######################################
# Author: 	Joost Vandorp, S. Smith	 #
# Revised: 	Thursday, Feb 24, 2017	 #
# Description:	"MAKEFILE"		 #
######################################

# Assumes JUnit is installed
# Assumes CLASSPATH has been set for Junit

JFLAGS = -g
#JCLASS = -cp ./src:.:$(CLASSPATH)
JCLASS = -cp ./src:.:$(CLASSPATH):/usr/share/java/junit4-4.5.jar # on mills
JC = javac
JVM = java
.SUFFIXES: .java .class
.java.class:
	$(JC) $(JFLAGS) $(JCLASS) $*.java

CLASSES = \
    src/ConnectionT.java \
    src/BoardT.java \
    src/Dots.java \
    src/DotT.java \

MAIN = Main

default: classes

classes: $(CLASSES:.java=.class)

doc:
	doxygen doxConfig
	cd latex && $(MAKE)

test: $(MAIN).class
	$(JC) $(JCLASS) $(JFLAGS) Main.java
	$(JVM) $(JCLASS) Main

# test: src/$(MAIN).class
# 	$(JVM) $(JCLASS) org.junit.runner.JUnitCore $(MAIN)

clean:
	rm -rf html
	rm -rf latex
	cd src
	rm **/*.class
