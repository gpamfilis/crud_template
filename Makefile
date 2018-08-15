
run:
	python manage.py runserver

pip-unistall:
	pip freeze | xargs pip uninstall -y

pip-install:
	pip install -r requirements3.txt

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf dist/
	@rm -rf *.egg
	@rm -rf *.egg-info


pull:
	git fetch --all
	git reset --hard origin/master
	sudo service apache2 reload

