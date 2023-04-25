<template>
    <div class="chat-container">
        <div class="chat-messages">
            <div v-for="message in messages" :key="message.id" class="chat-message" :class="{ 'is-me': message.isMe }">
                <span>{{ message.content }}</span>
            </div>
        </div>
        <div class="chat-input">
            <input ref="inputTextRef" v-model="inputText" type="text" placeholder="Type your message here..."
                :disabled="isSending" @keydown.enter="sendMessage" />
            <button :disabled="isSending" @click="sendMessage">{{ isSending ? 'Sending...' : 'Send' }}</button>
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
            isMe: true,
            isSending: false,
        }
    },
    methods: {
        async sendMessage() {
            if (this.inputText !== '') {
                this.messages.push({
                    id: this.messageId++,
                    content: this.inputText,
                    isMe: true,
                });

                this.isSending = true;

                try {

                    const response = await fetch('http://localhost:8000/chat', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ content: this.inputText }),
                    });

                    const result = await response.json();

                    this.messages.push({
                        id: this.messageId++,
                        content: result.content,
                        isMe: false,
                    });
                } catch (error) {
                    console.error(error);
                }

                this.inputText = '';
                this.isMe = true;
                this.isSending = false;

                // Focus the input box after the message is sent
                this.$nextTick(() => this.$refs.inputTextRef.focus())
            }
        }
    }
}
</script>
  
<style>
.chat-container {
    display: flex;
    flex-direction: column;
    height: 50vh;
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

.chat-input button:disabled {
    background-color: #ddd;
    color: #999;
    cursor: not-allowed;
}

.chat-input button:hover:not(:disabled) {
    background-color: #3e8e41;
    color: #fff;
}
</style>