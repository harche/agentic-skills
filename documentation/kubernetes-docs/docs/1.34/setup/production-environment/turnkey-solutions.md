# Turnkey Cloud Solutions

This page provides a list of Kubernetes certified solution providers. From each
provider page, you can learn how to install and setup production
ready clusters.

function updateLandscapeSource(button,shouldUpdateFragment) {
console.log({button: button,shouldUpdateFragment: shouldUpdateFragment});
try {
if(shouldUpdateFragment) {
window.location.hash = "#iframe-landscape-"+button.id;
} else {
var landscapeElements = document.querySelectorAll("#landscape");
let categories=button.dataset.landscapeTypes;
let link = `https://landscape.cncf.io/embed/embed.html?key=${encodeURIComponent(categories)}&headers=false&style=shadowed&size=md&bg-color=%23d95e00&fg-color=%23ffffff&iframe-resizer=true`
landscapeElements[0].src = link;
}
}
catch(err) {
console.log({message: "error handling Landscape switch", error: err})
}
}
document.addEventListener("DOMContentLoaded", function () {
let hashChangeHandler = () => {
if (window.location.hash) {
let selectedTriggerElements = document.querySelectorAll(".landscape-trigger"+window.location.hash);
if (selectedTriggerElements.length == 1) {
landscapeSource = selectedTriggerElements[0];
console.log("Updating Landscape source based on fragment:", window
.location
.hash
.substring(1));
updateLandscapeSource(landscapeSource,false);
}
}
}
var landscapeTriggerElements = document.querySelectorAll(".landscape-trigger");
landscapeTriggerElements.forEach(element => {
element.onclick = function() {
updateLandscapeSource(element,true);
};
});
var landscapeDefaultElements = document.querySelectorAll(".landscape-trigger.landscape-default");
if (landscapeDefaultElements.length == 1) {
let defaultLandscapeSource = landscapeDefaultElements[0];
updateLandscapeSource(defaultLandscapeSource,false);
}
window.addEventListener("hashchange", hashChangeHandler, false);
hashChangeHandler();
});

iFrameResize({ }, '#iframe-landscape');

## Feedback

Was this page helpful?

Yes
No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on
[Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes).
Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to
[report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io)
or
[suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).

const yes = document.querySelector('.feedback--yes');
const no = document.querySelector('.feedback--no');
document.querySelectorAll('.feedback--link').forEach(link => {
link.href = link.href + window.location.pathname;
});
const sendFeedback = (value) => {
if (!gtag) { console.log('!gtag'); }
gtag('event', 'click', {
'event_category': 'Helpful',
'event_label': window.location.pathname,
value
});
};
const disableButtons = () => {
yes.disabled = true;
yes.classList.add('feedback--button__disabled');
no.disabled = true;
no.classList.add('feedback--button__disabled');
};
yes.addEventListener('click', () => {
sendFeedback(1);
disableButtons();
document.querySelector('.feedback--response').classList.remove('feedback--response__hidden');
});
no.addEventListener('click', () => {
sendFeedback(0);
disableButtons();
document.querySelector('.feedback--response').classList.remove('feedback--response__hidden');
});

Last modified April 23, 2026 at 2:12 AM PST: [Merge pull request #55450 from sayanchowdhury/update-release-1.34-hugo.toml (d1f313a)](https://github.com/kubernetes/website/commit/d1f313a65f45bd4882d05fe9b6bea162fa2fdc16)
