# Viewing Site Analytics

This page contains information about the kubernetes.io analytics dashboard.

[View the dashboard](https://lookerstudio.google.com/u/0/reporting/fe615dc5-59b0-4db5-8504-ef9eacb663a9/page/4VDGB/).

This dashboard is built using [Google Looker Studio](https://lookerstudio.google.com/overview) and shows information collected on kubernetes.io using Google Analytics 4 since August 2022.

### Using the dashboard

By default, the dashboard shows all collected analytics for the past 30 days. Use the date selector to see data from a different date range. Other filtering options allow you to view data based on user location, the device used to access the site, the translation of the docs used, and more.

If you notice an issue with this dashboard, or would like to request any improvements, please [open an issue](https://github.com/kubernetes/website/issues/new/choose).

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
