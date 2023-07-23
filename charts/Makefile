.PHONY: install index debug pack clean
K8S_DEPLOY=
HELM=helm
K8S=$(K8S_DEPLOY) kubectl
install:
	@$(HELM) install $(app) $(app)
uninstall:
	@$(HELM) uninstall $(app) $(app)
upgrade:
	@$(HELM) upgrade --install $(app) $(app)
debug: 
	@$(HELM) template --debug $(app)
exec:
	@$(K8S) exec -it $(pod) --container $(container) -- /bin/bash
index:
	@$(HELM) repo index .
pack:
	@$(HELM) package $(app)
events:
	@$(K8S) get events --sort-by=.metadata.creationTimestamp --namespace=default
clean:
	@rm *.tgz
	@rm index.yaml
