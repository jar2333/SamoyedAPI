from src.book_scraper import BookScraper

def test_book_scraper_parser():
    html = """
        <div class="bigBoxContent containerWithHeaderContent" id="currentlyReadingReviews">
                    <div class="Updates no_border">
                <div class="firstcol">
                <a title="The Bell Jar" href="/book/show/6514.The_Bell_Jar"><img alt="The Bell Jar" src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1554582218l/6514._SX98_.jpg"></a>
                </div>
                <div class="secondcol">
                <div class="secondcol-top">
                    <div class="whos-review">
                    <div class="userReview">
                        <strong><a href="/user/show/73266776-mike-smith">Mike Smith</a></strong>
                        is currently reading
                    </div>
                    <div><a class="bookTitle" href="/book/show/6514.The_Bell_Jar">The Bell Jar</a></div>
                    <div>
                        <span class="by smallText">by</span> <a class="authorName" href="/author/show/4379.Sylvia_Plath">Sylvia Plath</a>
                    </div>

                        <div>
                            <span class="userReview">bookshelves: </span>
            <a class="actionLinkLite" href="https://www.goodreads.com/review/list/73266776-mike-smith?shelf=currently-reading">currently-reading</a>
        <br>

                        </div>
                    <div class="userReview">
                        <div class="greyText">
                        
                        </div>
                    </div>
                    </div>

                    <div class="rating" style="width:140px">
                    <div class="wtrButtonContainer" id="1_book_6514">
        <div class="wtrUp wtrLeft">
        <form action="/shelf/add_to_shelf" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="authenticity_token" value="3ptukMQvWGHGjsXZNwXxzfhmaa9ngEoWQBo4IzOUhUD5h+0MraS9QMxH2geigyi+l4FIVNAJg/ivKD5PwUVxgA==">
        <input type="hidden" name="book_id" id="book_id" value="6514">
        <input type="hidden" name="name" id="name" value="to-read">
        <input type="hidden" name="unique_id" id="unique_id" value="1_book_6514">
        <input type="hidden" name="wtr_new" id="wtr_new" value="true">
        <input type="hidden" name="from_choice" id="from_choice" value="false">
        <input type="hidden" name="from_home_module" id="from_home_module" value="false">
        <input type="hidden" name="ref" id="ref" value="" class="wtrLeftUpRef">
        <input type="hidden" name="existing_review" id="existing_review" value="false" class="wtrExisting">
        <input type="hidden" name="page_url" id="page_url">
        <button class="wtrToRead" type="submit">
        <span class="progressTrigger">Want to Read</span>
        <span class="progressIndicator">saving…</span>
        </button>
        </form>

        </div>

        <div class="wtrRight wtrUp">
        <form class="hiddenShelfForm" action="/shelf/add_to_shelf" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="authenticity_token" value="3ptukMQvWGHGjsXZNwXxzfhmaa9ngEoWQBo4IzOUhUD5h+0MraS9QMxH2geigyi+l4FIVNAJg/ivKD5PwUVxgA==">
        <input type="hidden" name="unique_id" id="unique_id" value="1_book_6514">
        <input type="hidden" name="book_id" id="book_id" value="6514">
        <input type="hidden" name="a" id="a">
        <input type="hidden" name="name" id="name">
        <input type="hidden" name="from_choice" id="from_choice" value="false">
        <input type="hidden" name="from_home_module" id="from_home_module" value="false">
        <input type="hidden" name="page_url" id="page_url">
        </form>

        <button class="wtrShelfButton"></button>
        <div class="wtrShelfMenu">
        <div class="wtrShelfList">
        <ul class="wtrExclusiveShelves">
        <li data-shelf-name="read">
        <button class="wtrExclusiveShelf" name="name" type="submit" value="read">
        <span class="progressTrigger">Read</span>
        <img alt="saving…" class="progressIndicator" src="https://s.gr-assets.com/assets/loading-trans-ced157046184c3bc7c180ffbfc6825a4.gif">
        </button>

        </li>
        <li data-shelf-name="currently-reading">
        <button class="wtrExclusiveShelf" name="name" type="submit" value="currently-reading">
        <span class="progressTrigger">Currently Reading</span>
        <img alt="saving…" class="progressIndicator" src="https://s.gr-assets.com/assets/loading-trans-ced157046184c3bc7c180ffbfc6825a4.gif">
        </button>

        </li>
        <li data-shelf-name="to-read">
        <button class="wtrExclusiveShelf" name="name" type="submit" value="to-read">
        <span class="progressTrigger">Want to Read</span>
        <img alt="saving…" class="progressIndicator" src="https://s.gr-assets.com/assets/loading-trans-ced157046184c3bc7c180ffbfc6825a4.gif">
        </button>

        </li>
        </ul>
        <ul class="wtrNonExclusiveShelves">
        <li data-shelf-name="cs">
        <label><img alt="loading…" class="progressIndicator" src="https://s.gr-assets.com/assets/loading-trans-ced157046184c3bc7c180ffbfc6825a4.gif">
        <input type="checkbox" name="name" id="name" value="cs" class="progressTrigger wtrNonExclusiveShelf">
        cs
        </label></li>

        <li data-shelf-name="queue">
        <label><img alt="loading…" class="progressIndicator" src="https://s.gr-assets.com/assets/loading-trans-ced157046184c3bc7c180ffbfc6825a4.gif">
        <input type="checkbox" name="name" id="name" value="queue" class="progressTrigger wtrNonExclusiveShelf">
        queue
        </label></li>

        <li data-shelf-name="writing">
        <label><img alt="loading…" class="progressIndicator" src="https://s.gr-assets.com/assets/loading-trans-ced157046184c3bc7c180ffbfc6825a4.gif">
        <input type="checkbox" name="name" id="name" value="writing" class="progressTrigger wtrNonExclusiveShelf">
        writing
        </label></li>

        </ul>
        <div class="wtrShelfSearchAddShelf">
        <form autocomplete="off" action="https://www.goodreads.com/shelf/add_to_shelf" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="authenticity_token" value="3ptukMQvWGHGjsXZNwXxzfhmaa9ngEoWQBo4IzOUhUD5h+0MraS9QMxH2geigyi+l4FIVNAJg/ivKD5PwUVxgA==">
        <input type="hidden" name="unique_id" id="unique_id">
        <input type="hidden" name="book_id" id="book_id">
        <button class="progressTrigger" name="name" type="submit" value="">
        Add "<span class="wtrButtonLabelShelfName"></span>" Shelf
        </button>
        <img alt="saving…" class="progressIndicator" src="https://s.gr-assets.com/assets/loading-trans-ced157046184c3bc7c180ffbfc6825a4.gif">
        </form>

        </div>
        </div>
        <div class="wtrOtherShelfOptions">
        <label class="wtrExclusiveShelf wtrAddShelf" for="add_shelf_1_book_6514">Add shelf</label>
        <form class="wtrAddShelf gr-form gr-form--compact" autocomplete="off" action="https://www.goodreads.com/shelf/add_to_shelf" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="authenticity_token" value="3ptukMQvWGHGjsXZNwXxzfhmaa9ngEoWQBo4IzOUhUD5h+0MraS9QMxH2geigyi+l4FIVNAJg/ivKD5PwUVxgA==">
        <input type="hidden" name="unique_id" id="unique_id">
        <input type="hidden" name="book_id" id="book_id">
        <input type="hidden" name="from_choice" id="from_choice" value="false">
        <input type="text" name="name" id="add_shelf_1_book_6514" autocorrect="off" autocomplete="off">
        <img alt="saving…" class="progressIndicator" src="https://s.gr-assets.com/assets/loading-trans-ced157046184c3bc7c180ffbfc6825a4.gif">
        <button name="button" type="submit" class="gr-form--compact__submitButton progressTrigger">Add</button>
        </form>

        </div>
        </div>
        </div>

        <div class="ratingStars wtrRating">
        <div class="starsErrorTooltip hidden">
        Error rating book. Refresh and try again.
        </div>
        <div class="myRating uitext greyText">Rate this book</div>
        <div class="clearRating uitext" style="display: none;">Clear rating</div>
        <div class="stars" data-resource-id="6514" data-user-id="175481810" data-submit-url="/review/rate/6514?stars_click=true&amp;wtr_button_id=1_book_6514" data-rating="0" data-restore-rating="null"><a class="star off" title="did not like it" href="#" ref="">1 of 5 stars</a><a class="star off" title="it was ok" href="#" ref="">2 of 5 stars</a><a class="star off" title="liked it" href="#" ref="">3 of 5 stars</a><a class="star off" title="really liked it" href="#" ref="">4 of 5 stars</a><a class="star off" title="it was amazing" href="#" ref="">5 of 5 stars</a></div>
        </div>

        </div>

                    </div>
                </div>



                <br class="clear">

                <div>
              <span class="left greyText">progress:&nbsp;</span>
              
    <div class="graphContainer progressGraph" style="width: 130px;">
      <div style="width: 4%;" class="graphBar">&nbsp;</div>
  </div>

  &nbsp;
    <a onclick="if (typeof(clickPageOfBook) == 'function') {clickPageOfBook(594288, , {viewLink: '<a class=\&quot;greyText\&quot; href=\&quot;https://www.goodreads.com/user_status/show/813489194\&quot;>Mar 26, 2024 11:47PM<\/a>'});return false;};" class="greyText smallText" href="https://www.goodreads.com/user_status/show/813489194">(4%)</a>

  <br class="clear">
    <span class="readable">
      "Finished chapter 1, it was an overview"
    </span>


<span class="greyText">—</span>
<a class="greyText" href="https://www.goodreads.com/user_status/show/813489194">Mar 26, 2024 11:47PM</a>

            </div>

                <br class="clear">
                <table>
                

        <tbody><tr class="no_border feedFooterReview" id="update_comment_stuff_Review4917911731">
            <td>&nbsp;</td>
        <td colspan="2">
            <div class="updateActionLinks">





                            <a class="updatedTimestamp" ref="timestamp" href="/review/show/4917911731">Sept 30, 2019 09:00AM</a>
        &nbsp;·&nbsp;<a id="commentLink_4917911731" href="#" onclick="comment_form_for('review', 4917911731, true, ''); return false;">comment</a>
            </div>


            <div id="comments_for_review_4917911731" style="display: none;">
        </div>
        <div class="brown_comment" id="comments_form_review_4917911731" style="display: none">
        <textarea class="placeholder_text" onclick="expand_comment_form_for('review', 4917911731, true, '')">Write a comment...</textarea>
        </div>

        </td>
        </tr>

                </tbody></table>
            </div>
            </div>


        <div class="clear"></div></div>

    """

    scraper = BookScraper()

    responses = scraper.parse(html)

    assert {
            "title": "The Bell Jar",
            "url": "http://goodreads.com/book/show/6514.The_Bell_Jar",
            "author": "Sylvia Plath",
            "author_url": "http://goodreads.com/author/show/4379.Sylvia_Plath",
            "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1554582218l/6514._SX98_.jpg",
            "progress": "4"
    } == responses[0]