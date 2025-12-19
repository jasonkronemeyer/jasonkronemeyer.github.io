const puppeteer = require('puppeteer-core');
(async ()=>{
  try{
    const browser = await puppeteer.launch({executablePath: '/usr/bin/chromium-browser', args:['--no-sandbox','--disable-setuid-sandbox']});
    const page = await browser.newPage();
    page.on('console', msg => console.log('PAGE LOG:', msg.text()));
    page.on('pageerror', err => console.log('PAGE ERROR:', err.message));
    await page.goto('http://127.0.0.1:8000/knowledge%20modeling/semantic%20web/digital%20equity/2025/12/18/knowledge-modeler.html', {waitUntil: 'networkidle0'});
    // wait a bit to capture any delayed errors
    await page.waitForTimeout(2000);
    console.log('page loaded');
    await browser.close();
  }catch(e){console.error('ERR',e);} 
})();