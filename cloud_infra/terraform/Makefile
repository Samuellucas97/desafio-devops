all: preparation
.PHONY: all preparation run

	
preparation: clean
	@echo
	@echo "******************** PREPARING TERRAFORM ENVIRONMENT **********************************"
	terraform init
	@echo
	@echo
	@echo "******************** REVISING THE CLOUD INFRAESTRUCTURE PLAN **********************************"
	terraform plan -out=tfplan
	@echo


run: preparation	 
	@echo
	@echo "******************** APPLYING THE CLOUD INFRAESTRUCTURE PLAN **********************************"
	terraform apply
	@echo


clean:
	@echo
	@echo "******************** DESTROYING CLOUD INFRAESTRUCTURE **********************************"
	terraform destroy -auto-approve
	@echo
	


