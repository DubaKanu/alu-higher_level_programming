#!/usr/bin/node

const fs = require('fs');

// Get the file path from command line arguments
const filePath = process.argv[2];

// Read the file
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
