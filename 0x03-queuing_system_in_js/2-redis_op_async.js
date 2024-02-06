import { createClient } from 'redis';
import { print } from 'redis';
import { promisify } from 'util'

const client = createClient();

client.on('error', err => console.log(`Redis client not connected to the server: ${err.message}`));
client.on('connect', () => console.log('Redis client connected to the server'))

client.connect

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, function (res, data) {
    print(`Reply: ${data}`)
  });
}

const displaySchoolValue = promisify((schoolName) => {
  client.get(schoolName, function (res, data) {
    console.log(data);
  })
})

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
