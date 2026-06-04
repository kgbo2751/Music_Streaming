function playAudio(index){
    const audio = document.getElementById(`audio-${index}`);
    audio.play();
    updateProgress(index);
}

function pauseAudio(index){
    const audio = document.getElementById(`audio-${index}`);
    audio.pause();
}

function updateProgress(index){
    const audio = document.getElementById(`audio-${index}`);
    const progress = document.getElementById(`progress-${index}`);
    const currentTime = document.getElementById(`current-${index}`);
    const duration = document.getElementById(`duration-${index}`);

    duration.textContent = formatTime(audio.duration || 0);

    const interval = setInterval(() => {
        if(audio.paused || audio.ended){
            clearInterval(interval);
        } else {
            currentTime.textContent = formatTime(audio.currentTime);
            const percent = (audio.currentTime / audio.duration) * 100;
            progress.style.width = percent + "%";
        }
    }, 500);
}

function seekAudio(event, index){
    const audio = document.getElementById(`audio-${index}`);
    const bar = event.currentTarget;
    const rect = bar.getBoundingClientRect();
    const percent = (event.clientX - rect.left) / rect.width;
    audio.currentTime = percent * audio.duration;
}

function formatTime(sec){
    const minutes = Math.floor(sec / 60);
    const seconds = Math.floor(sec % 60);
    return `${minutes}:${seconds.toString().padStart(2, '0')}`;
}