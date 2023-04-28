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
import { nextTick, ref, type Ref } from 'vue'

var inputText = ''
var isSending = false
var messages: Ref<{ id: number, content: string, isMe: boolean }[]> = ref([])
var messageId = 0
const inputTextRef: Ref<HTMLInputElement | null> = ref(null);

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
        isSending = true;
        console.log('Sending message: ' + messageToSend);
        try {
            const response = await fetch('http://localhost:8000/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ content: messageToSend }),
            });
            const result = await response.json();
            messages.value.push({
                id: messageId++,
                content: result.content,
                isMe: false,
            });
        } catch (error) {
            console.error(error);
        }
        isSending = false;
        // Focus the input box after the message is sent
        nextTick(() => inputTextRef.value?.focus())
    }
}
</script>
