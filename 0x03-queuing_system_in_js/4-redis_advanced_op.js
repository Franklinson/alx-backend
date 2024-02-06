import { createClient } from 'redis';
import { print } from 'redis';
import { promisify } from 'util'

const client = createClient();

client.on('error', err => console.log(`Redis client not connected to the server: ${err.message}`));
client.on('connect', () => console.log('Redis client connected to the server'))

client.connect

const obj = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2,
}

for (const key of Object.keys(obj)) {
  client.hset('HolbertonSchools', key, obj[key], (res, data) => {
    print(`Reply: ${data}`);
  })
}

client.hgetall('HolbertonSchools', (res, data) => {
  console.log(data)
})
