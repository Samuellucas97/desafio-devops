all: run
.PHONY: all build run clean

requirements:
	@echo
	@echo "******************** INSTALLING SOFTWARE REQUIREMENTS **********************************"
	if [ -x /usr/bin/apt-get ]; then  xargs -a requirements.txt sudo apt-get install -y; fi
	@echo
	@echo
	
build: clean
	@echo
	@echo "******************** BUILDING THE VIRTUAL MACHINE **********************************"
	vagrant provision
	@echo
	vagrant status
	@echo


run: build	 
	@echo
	@echo "******************** RUNNING THE VIRTUAL MACHINE **********************************"
	vagrant up
	@echo
	vagrant status
	@echo
	vagrant ssh
	@echo


clean:
	@echo
	@echo "******************** DESTROYING THE VIRTUAL MACHINE **********************************"
	vagrant destroy -f
	@echo
	vagrant status
	@echo
	


