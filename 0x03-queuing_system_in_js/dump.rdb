import redis from 'redis';

// Create a Redis client.
const client = redis.createClient();

// Listen for the 'connect' event.
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Listen for the 'error' event.
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Gracefully close the redis connection when the script exits.
process.on('SIGINT', () => {
  client.quit();
});

// Gracefully close the redis connection when the script exit.
process.on('SIGTERM', () => {
  client.quit();
});
