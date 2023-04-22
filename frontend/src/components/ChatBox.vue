<template>
    <div class="chat-container">
        <div class="chat-messages">
            <div v-for="message in messages" :key="message.id" class="chat-message" :class="{ 'is-me': message.isMe }">
                <span>{{ message.content }}</span>
            </div>
        </div>
        <div class="chat-input">
            <input v-model="inputText" type="text" placeholder="Type your message here..." @keydown.enter="sendMessage" />
            <button @click="sendMessage">Send</button>
        </div>
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            inputText: '',
            messages: [],
            messageId: 0,
            isMe: true
        }
    },
    methods: {
        sendMessage() {
            if (this.inputText !== '') {
                this.messages.push({
                    id: this.messageId++,
                    content: this.inputText,
                    isMe: this.isMe
                })
                this.inputText = ''
                this.isMe = !this.isMe
            }
        }
    }
}
</script>
  
<style>
.chat-container {
    display: flex;
    flex-direction: column;
    height: 100vh;
}

.chat-messages {
    flex: 1;
    overflow-y: auto;
}

.chat-message {
    display: flex;
    justify-content: center;
    align-items: center;
    max-width: 80%;
    margin: 10px;
    padding: 10px;
    border-radius: 10px;
    background-color: #f3f3f3;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.chat-message.is-me {
    align-self: flex-end;
    background-color: #dcf8c6;
}

.chat-input {
    display: flex;
    align-items: center;
    padding: 10px;
    background-color: #fff;
    box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.2);
}

.chat-input input {
    flex: 1;
    margin-right: 10px;
    padding: 10px;
    border: none;
    border-radius: 10px;
    background-color: #f3f3f3;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.chat-input button {
    padding: 10px;
    border: none;
    border-radius: 10px;
    background-color: #4caf50;
    color: #fff;
    cursor: pointer;
    transition: background-color 0.2s ease;
}

.chat-input button:hover {
    background-color: #3e8e41;
}
</style>
  