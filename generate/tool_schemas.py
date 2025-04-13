tool_schema = [
    {
      "type": "function",
      "name": "generate_image",
      "description": "Generate an image using OpenAI DALL·E 3 based on a prompt",
      "parameters": {
        "type": "object",
        "required": [
          "prompt",
          "num_images",
          "size"
        ],
        "properties": {
          "prompt": {
            "type": "string",
            "description": "The textual description to generate the image from"
          },
          "num_images": {
            "type": "number",
            "description": "The number of images to generate"
          },
          "size": {
            "type": "string",
            "description": "The size of the generated image, e.g., '1024x1024'",
            "enum": [
              "256x256",
              "512x512",
              "1024x1024"
            ]
          }
        },
        "additionalProperties": False
      },
      "strict": True
    },
    {
      "type": "web_search_preview",
      "user_location": {
        "type": "approximate"
      },
      "search_context_size": "medium"
    }
  ]