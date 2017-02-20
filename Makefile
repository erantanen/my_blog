PY?=python3
PELICAN?=pelican


BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py


#############################
# beginning of targets
############################

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)


devserver:
ifdef PORT
	$(BASEDIR)/develop_server.sh restart $(PORT)
else
	$(BASEDIR)/develop_server.sh restart
endif

####################################
# building all content under putput
####################################

build:
	$(MAKE) clean
	$(MAKE) html
	-cp -R code_snips output/code_snips/
	
tar:
	-tar cfv output.tar output

.PHONY: html clean build tar devserver 
