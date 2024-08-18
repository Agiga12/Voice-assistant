const chatContainer = document.getElementById('chat-container');
const userInput = document.getElementById('userInput');

function insertUserMessage(message) {
    const userMessage = document.createElement('p');
    userMessage.textContent = message;
    userMessage.className = 'user-message';
    chatContainer.appendChild(userMessage);
}

function insertAssistantMessage(message) {
    const assistantMessage = document.createElement('p');
    assistantMessage.textContent = message;
    assistantMessage.className = 'assistant-message';
    chatContainer.appendChild(assistantMessage);
}

function listenCommand() {
    // Your speech recognition code here
    try {
        with (speech_recognition.Microphone() as mic) {
            sr.adjust_for_ambient_noise(source=mic, duration=0.5);
            audio = sr.listen(source=mic);
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower();
        }
        return query;
    } catch (speech_recognition.UnknownValueError) {
        return 'Не понятно:(';
    }
}

function chatt() {
    const messages = [
        SystemMessage(
            content=" "
        )
    ];
    const voice = pyttsx3.init();
    voice.say('Здравствуйте, как ваше настроение?');
    voice.runAndWait();
    insertAssistantMessage('Здравствуйте, как ваше настроение?');
    while (true) {
        const user_input = listenCommand();
        messages.push(HumanMessage(content=user_input));
        insertUserMessage(user_input);

        const response = chat(messages);
        messages.append(response);
        const response_text = response.content;

        console.log("Bot:", response_text);
        insertAssistantMessage(response_text);

        const engine = pyttsx3.init();
        engine.say(response_text);
        engine.runAndWait();

        if (user_input === "выключись") {
            break;
        }
    }
}

userInput.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        insertUserMessage(userInput.value);
        userInput.value = '';
        // Add logic here for the virtual assistant's response
        insertAssistantMessage("Это ответ от виртуального ассистента.");
    }
});
