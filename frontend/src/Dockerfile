# Use Node.js base image
FROM node:16

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json ./
RUN npm install

# Copy all files
COPY . .

# Expose frontend port
EXPOSE 3000

# Run the app
CMD ["npm", "start"]
