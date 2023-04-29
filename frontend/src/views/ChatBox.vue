<template>
    <div class="container">
        <div class="row">
            <div class="col-md-12" v-for="message in messages" :key="message.id">
                <div class="row mb-2" :class="{ 'justify-content-end': message.isMe }">
                    <div class="col-md-6 p-2" :class="{ 'bg-primary text-white': message.isMe, 'bg-light': !message.isMe }">
                        <span>{{ message.content }}</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <div class="input-group">
                    <input v-model="inputText" ref="inputTextRef" type="text" class="form-control"
                        placeholder="Type your message here..." :disabled="isSending" @keydown.enter="sendMessage" />
                    <div class="input-group-append">
                        <button :disabled="isSending" class="btn btn-primary" type="button" @click="sendMessage">{{
                            isSending ? 'Sending...' : 'Sent' }}</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, type Ref, onBeforeUnmount } from 'vue'

var inputText = ''
var isSending = false
var messages: Ref<{ id: number, content: string, isMe: boolean }[]> = ref([])
var messageId = 0
const inputTextRef = ref<HTMLInputElement | null>(null);
const ws = ref<WebSocket | null>(null);

ws.value = new WebSocket('ws://localhost:8000/chat/ws');

ws.value.onmessage = (event) => {

    const message = event.data
    messages.value.push({
        id: messageId++,
        content: message,
        isMe: false,
    });
};

ws.value.onclose = () => {
    console.log('WebSocket connection closed');
};

ws.value.onerror = (error) => {
    console.error(error);
};

onBeforeUnmount(() => {
    if (ws.value?.readyState === WebSocket.OPEN) {
        ws.value?.close();
    }
});

async function sendMessage() {
    if (inputText !== '') {
        // clear out the text field
        var messageToSend = inputText
        inputText = ''

        messages.value.push({
            id: messageId++,
            content: messageToSend,
            isMe: true,
        });
        console.log('Sending message: ' + messageToSend);
        ws.value?.send(JSON.stringify({ content: messageToSend }));
    }
}
</script>
