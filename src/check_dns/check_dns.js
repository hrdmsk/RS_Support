const dns = require('dns');

function queryDns(domain) {
  console.log(`DNS records for ${domain}:`);

  dns.resolve(domain, 'A', (err, addresses) => {
    if (err) {
      console.error(`Error resolving A records: ${err}`);
      return;
    }
    console.log('A records:', addresses);
  });

  dns.resolve(domain, 'AAAA', (err, addresses) => {
    if (err) {
      console.error(`Error resolving AAAA records: ${err}`);
      return;
    }
    console.log('AAAA records:', addresses);
  });

  dns.resolve(domain, 'MX', (err, addresses) => {
    if (err) {
      console.error(`Error resolving MX records: ${err}`);
      return;
    }
    console.log('MX records:', addresses);
  });

  dns.resolve(domain, 'CNAME', (err, addresses) => {
    if (err) {
      console.error(`Error resolving CNAME records: ${err}`);
      return;
    }
    console.log('CNAME records:', addresses);
  });

  dns.resolve(domain, 'NS', (err, addresses) => {
    if (err) {
      console.error(`Error resolving NS records: ${err}`);
      return;
    }
    console.log('NS records:', addresses);
  });

  dns.resolve(domain, 'TXT', (err, addresses) => {
    if (err) {
      console.error(`Error resolving TXT records: ${err}`);
      return;
    }
    console.log('TXT records:', addresses);
  });
}

// 使用例: ドメインを指定してDNSレコードを出力
const domain = 'example.com'; // ここにドメインを指定してください
queryDns(domain);