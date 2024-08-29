
### USAGE.md

# Usage Guide

This guide will help you use the Social Media Manager Assistant to generate and manage social media content.

## Setup

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up your environment variables:
   ```
   export OPENAI_API_KEY=your_api_key_here
   ```

## Running the Assistant

To run the assistant, use the following command:

```
python app/main.py
```

or interact through API endpoints (forthcoming).

## Generating a Post

### CLI

1. Select a profile:
   ```
   Enter profile name (e.g., profile_a): 
   ```

2. Enter a topic:
   ```
   Enter topic for the new post: 
   ```

3. The assistant will generate a new post based on the selected profile's previous posts and the given topic.

### API endpoint

To generate a post, send a POST request to the `/generate_post` endpoint with the following JSON body:

```json
{
  "topic": "Artificial Intelligence in Marketing",
  "profile_id": "12345"
}
```

The response will include the generated post text:

```json
{
  "post": "Artificial Intelligence is revolutionizing marketing by enabling personalized customer experiences..."
}
```

## Managing Profiles

To add a new profile:

1. Create a new directory under `data/profiles/` with the profile name.
2. Add a `previous_posts.json` file in the new directory with the following structure:
   ```json
   [
     {
       "content": "This is a previous post.",
       "timestamp": "2023-08-23T12:00:00Z"
     }
   ]
   ```

### API endpoint

Profiles allow you to define the tone and style of your content. Use the /manage_profile endpoint to create, update, or delete profiles.

#### Creating a Profile
```json
{
  "action": "create",
  "profile_name": "Tech Innovators",
  "tone": "Professional",
  "style": "Insightful"
}
```
#### Updating a Profile
```json
{
  "action": "update",
  "profile_id": "12345",
  "tone": "Conversational"
}
```
#### Deleting a Profile
```json
{
  "action": "delete",
  "profile_id": "12345"
}
```
## Storing and Retrieving Posts
The system automatically stores posts in the Chroma vector database to prevent duplication.

### Storing a Post
To manually store a post, use the /store_post endpoint:

```json
{
  "post": "Artificial Intelligence is revolutionizing marketing...",
  "profile_id": "12345"
}
```
The system will confirm the storage and return a post ID:

```json
{
  "post_id": "67890"
}
```

## Viewing Generated Posts

Generated posts will be displayed in the console and also stored in the SQLite database for future reference.

## Troubleshooting

If you encounter any issues, please check the following:

1. Ensure all dependencies are installed correctly.
2. Verify that your API key is set correctly.
3. Check that the profile directories and files are structured correctly.

For more detailed information, refer to the README.md file.