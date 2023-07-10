from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Get the livestream ID from the URL or request parameters
        self.livestream_id = self.scope['url_route']['kwargs']['livestream_id']

        # Add the consumer to the specific livestream group
        await self.channel_layer.group_add(
            self.livestream_id,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Remove the consumer from the livestream group when disconnected
        await self.channel_layer.group_discard(
            self.livestream_id,
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle incoming chat messages
        message = json.loads(text_data)
        content = message['content']
        
        # Broadcast the message to the entire livestream group
        await self.channel_layer.group_send(
            self.livestream_id,
            {
                'type': 'chat_message',
                'content': content,
            }
        )

    async def chat_message(self, event):
        # Send the chat message to the WebSocket
        content = event['content']
        await self.send(text_data=json.dumps({
            'content': content,
        }))
