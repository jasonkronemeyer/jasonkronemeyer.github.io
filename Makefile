# Makefile for common Jekyll tasks

install:
	bundle install
	npm install --no-save @mermaid-js/mermaid-cli

build:
	bundle exec jekyll build --trace

# Use system Chromium for Puppeteer-based plugins (jekyll-diagrams)
# Exports ensure Puppeteer uses the installed browser and disables sandboxing
build-chrome:
	export PUPPETEER_EXECUTABLE_PATH=$(shell which chromium || which chromium-browser || which google-chrome-stable) ; \
	export PUPPETEER_ARGS='--no-sandbox --disable-setuid-sandbox' ; \
	bundle exec jekyll build --trace

# Mirrors GitHub Actions build steps for local parity
build-gha-compatible:
	npm install --no-save @mermaid-js/mermaid-cli
	npx puppeteer install
	export PATH=$(PWD)/node_modules/.bin:$$PATH ; \
	export PUPPETEER_EXECUTABLE_PATH=$$(command -v chromium || command -v chromium-browser || command -v google-chrome-stable) ; \
	export PUPPETEER_ARGS='--no-sandbox --disable-setuid-sandbox' ; \
	bundle exec jekyll build --trace -d ./_site

serve:
	bundle exec jekyll serve --drafts --livereload

clean:
	rm -rf _site .jekyll-cache

deploy-gh-pages:
	# placeholder for future deployment steps
	echo "Add deployment steps here"