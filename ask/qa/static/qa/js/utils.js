function handleQuestionLikeBtn(btn) {
  $.ajax({
    method: 'POST',
    url: document.getElementById('questionLikeBtnUrl').value,
    data: {
      question_id: btn.val(),
      csrfmiddlewaretoken: $.cookie('csrftoken'),
    },
    success: function(json) {
      if(json['code'] == 'no_auth') {
        $(`#alertPlaceholder${btn.val()}`).append(
          '<div class="alert alert-warning" role="alert">' +
          `Please <a href="${document.getElementById('questionLikeBtnLoginUrl').value}" class="alert-link">log in</a> to rate questions.` +
          '</div>'
        );
      }
      else 
        document.getElementById(`question_rating${btn.val()}`).innerHTML = json['rating']
    },
    error: function() {
      $(`#alertPlaceholder${btn.val()}`).append(
        '<div class="alert alert-danger" role="alert">' +
        'Oops! Rated question not found' +
        '</div>'
      );
    }
  });
}