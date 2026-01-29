# Makefile for common Jekyll tasks

install:
	bundle install

build:
	bundle exec jekyll build --trace

serve:
	bundle exec jekyll serve --drafts --livereload

clean:
	rm -rf _site .jekyll-cache

deploy-gh-pages:
	# placeholder for future deployment steps
	echo "Add deployment steps here"