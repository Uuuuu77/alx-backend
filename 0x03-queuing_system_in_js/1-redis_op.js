// 1-redis_op.js

import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

process.on('SIGINT', () => {
  client.quit();
});

process.on('SIGTERM', () => {
  client.quit();
});

// Function to set a new school value in Redis
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

// Function to display the value for a given school key
const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, value) => {
    if (err) {
      console.error(`Error retrieving value for key ${schoolName}: ${err}`);
      return;
    }
    console.log(value);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
