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
                    <input v-model="inputText" ref="inputTextRef" type="text" class="form-control" placeholder="Type your message here..."
                        :disabled="isSending" @keydown.enter="sendMessage" />
                    <div class="input-group-append">
                        <button :disabled="isSending" class="btn btn-primary" type="button" @click="sendMessage">{{
                            isSending ? 'Sending...' : 'Sent' }}</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            inputText: '',
            messageToSend: '',
            messages: [],
            messageId: 0,
            isMe: true,
            isSending: false,
        };
    },
    methods: {
        async sendMessage() {
            if (this.inputText !== '') {

                // clear out the text field
                this.messageToSend = this.inputText
                this.inputText = ''

                this.messages.push({
                    id: this.messageId++,
                    content: this.messageToSend,
                    isMe: true,
                });
                this.isSending = true;
                try {
                    const response = await fetch('http://localhost:8000/chat', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ content: this.messageToSend }),
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
                this.isSending = false;
                // Focus the input box after the message is sent
                this.$nextTick(() => this.$refs.inputTextRef.focus())
            }
        }
    },
};
</script>

<style></style>
