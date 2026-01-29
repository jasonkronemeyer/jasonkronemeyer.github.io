# Makefile for common Jekyll tasks

install:
	bundle install

build:
	bundle exec jekyll build --trace

# Use system Chromium for Puppeteer-based plugins (jekyll-diagrams)
# Exports ensure Puppeteer uses the installed browser and disables sandboxing
build-chrome:
	export PUPPETEER_EXECUTABLE_PATH=$(shell which chromium-browser || which chromium || which google-chrome-stable) ; \
	export PUPPETEER_ARGS='--no-sandbox --disable-setuid-sandbox' ; \
	bundle exec jekyll build --trace

serve:
	bundle exec jekyll serve --drafts --livereload

clean:
	rm -rf _site .jekyll-cache

deploy-gh-pages:
	# placeholder for future deployment steps
	echo "Add deployment steps here"