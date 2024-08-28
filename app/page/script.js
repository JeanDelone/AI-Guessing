document.addEventListener('DOMContentLoaded', () => {
    const photoElement = document.getElementById('photo');
    const voteAiButton = document.getElementById('vote-ai');
    const voteNotAiButton = document.getElementById('vote-not-ai');
    const resultElement = document.getElementById('result');

    // Function to fetch a random image
    function fetchRandomImage() {
        fetch('/images/random')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to fetch image');
                }
                return response.json();
            })
            .then(image => {
                // Construct the correct image path using the image ID
                const imagePath = `../../pictures/${image.id}.jpeg`;
                
                // Set the image source to the constructed path
                photoElement.src = imagePath;
                photoElement.style.display = 'block';
                voteAiButton.style.display = 'inline';
                voteNotAiButton.style.display = 'inline';

                // Store image ID for vote submission
                photoElement.dataset.imageId = image.id;
            })
            .catch(error => {
                resultElement.textContent = 'Error: ' + error.message;
            });
    }

    // Function to send a vote
    function sendVote(isAi) {
        const imageId = photoElement.dataset.imageId;
        const voteData = {
            image_id: imageId,
            user_vote: isAi
        };

        fetch('/vote', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(voteData)
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to submit vote');
                }
                return response.json();
            })
            .then(vote => {
                resultElement.textContent = `Your vote for image ${vote.image_id} was recorded.`;
                photoElement.style.display = 'none';
                voteAiButton.style.display = 'none';
                voteNotAiButton.style.display = 'none';
            })
            .catch(error => {
                resultElement.textContent = 'Error: ' + error.message;
            });
    }

    // Event listeners for buttons
    voteAiButton.addEventListener('click', () => sendVote(true));
    voteNotAiButton.addEventListener('click', () => sendVote(false));

    // Fetch a random image when the page loads
    fetchRandomImage();
});
