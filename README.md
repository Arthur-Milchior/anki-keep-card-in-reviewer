# Keep card in reviewer
## Rationale
Sometime, I want to keep seing a card in the reviewer instead of seing
"Waiting for editing to finish." This is in particular the case when
the edit in the browser is not related at all to the current reviewed
card.

This add-on simply ensure this, as long as the note of the card in the
reviewer has not been deleted or modified, it stays displayed.

You may also want to install add-on ("edited" value of note is not changed unless card is really edited.)[https://ankiweb.net/shared/info/153450853] to ensure that note are not seen as edited unless they really are.

## Warning

### Error message
There may be a lot of thing I didn't take into account. I don't expect
the add-on to ever create any serious trouble. However, it is possible
that you see an error message if there is something I forget to take
into account. Please let me know.

## Bad card order
It is possible that some change that you make to a note would have
changed the order in which cards should have been displayed. Since the
reviewer does not stop showing current card, it never recomputes the
order of cards to show. If you want to force a recomputation, you need
to start reviewing again (you can do it by pressing "s" in the
reviewer, for example). Most of the time however, that should not be a
problem you have to take into consideration.

This would be the case in particular if you unsuspended a card or if
you changed a note so that anki generates a new card. In both case,
without this add-on, the button "resume now" may show a card which
is different from the one you were seing before opening editor/browser.

## Internal
It modifies AnkiQt.requireReset and call the previous version of the method.

## TODO
Ensure that a note is marked as modified only if it is modified, and
not only when the focus is in the note's field.

## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-keep-card-in-reviewer
Addon number| [1894745652](https://ankiweb.net/shared/info/1894745652)
Support me on| [![Ko-fi](https://ko-fi.com/img/Kofi_Logo_Blue.svg)](Ko-fi.com/arthurmilchior) or [![Patreon](http://www.milchior.fr/patreon.png)](https://www.patreon.com/bePatron?u=146206)
