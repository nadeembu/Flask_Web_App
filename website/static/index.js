/* Take the noteID that was passed to the deleteNote function
and send a post request to the delete note endpoint. 
Then window.location.href will reload the window.
 */
function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }