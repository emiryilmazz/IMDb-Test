BASE_URL = "https://www.imdb.com"

#--------------------------------------------------------------------"LOCATERS"------------------------------------------------------------------------------------

#------------------------------------------------------US01-Search-----------------------------------------------------------------------------

#------------------------test_movie_search-------------

Movie_Search_XPATH = "The Lord of the Rings: The Fellowship of the Ring"
Movie_Search_Name_Screenshot = "Images/movie_search_name.png"
Search_Result_Movie_Name_XPATH = "//div[@id='react-autowhatever-navSuggestionSearch']//ul[@role='listbox']/li[1]//div[.='The Lord of the Rings: The Fellowship of the Ring']"
Movie_Search_Detail_Screenshot = "Images/movie_detail.png"

#------------------------test_director_name--------------------------

Director_Name_Search_XPATH = "Christopher Nolan"
Director_Name_Screenshot = "Images/director_detail.png"
Director_Name_Result_XPATH = "//div[@id='react-autowhatever-navSuggestionSearch']//ul[@role='listbox']/li[1]//div[.='Christopher Nolan']"


#------------------------test_actor_name-----------------------------
Actor_Search_XPATH = "Robert Downey Jr."
Search_Result_Actor_Name_XPATH = "//div[@id='react-autowhatever-navSuggestionSearch']//ul[@role='listbox']/li[1]//div[.='Robert Downey Jr.']"
Actor_Name_Screenshot = "Images/actor_detail.png"



#------------------------------------------------------US02-Empty_Search-----------------------------------------------------------------------------

#------------------------test_empty_search-------------------------

Empty_Search_XPATH = "//*[@id='suggestion-search-button']"
Empty_Search_Screenshot = "Images/empty_search.png"
Empty_Search_Text_XPATH = "//*[@id='__next']/main/div[2]/div[3]/section/div/div[1]/section[1]/h1"
Empty_Search_Text_Assert = "Search IMDb"  





#-------------------------------------------------------US03-Filter_Options------------------------------------------------------------------------

#------------------------test_filter_titles-------------------------
All_Button_XPATH = "//*[@id='nav-search-form']/div[1]"
Select_All_Titles_XPATH = "//span[@id='navbar-search-category-select-contents']/ul[@role='menu']/li[2]/span[@role='presentation']"
Search_Result_Movie_Title_XPATH = "//div[@id='react-autowhatever-navSuggestionSearch']//ul[@role='listbox']/li[1]//div[.='Dune']"
Test_Filter_Searchbar_Entry = "Dune 2021" 
Test_Filter_Titles_Screenshot = "Images/movie_dune.png"

#------------------------test_filter_tv_episode----------------------
Select_Tv_Episode_XPATH = "//span[@id='navbar-search-category-select-contents']/ul[@role='menu']/li[3]/span[@role='presentation']"
Tv_Episode_Searchbar_Entry = "The Last of Us" 
tv_episode_dropdownlist_XPATH = "//*[@id='react-autowhatever-navSuggestionSearch--item-0']/a"
tv_episode_dropdownlist_text = "The Last of Us", "The Last of Us does not appear in the drop-down list"
Tv_episode_screenshot = "Images/test_filter_tv_episode_error.png"
Tv_episode_assertion_error_text = "An error occurred while waiting for the element: "

#------------------------test_fiter_celebs--------------------------
select_celebs_xpath = "//span[@id='navbar-search-category-select-contents']/ul[@role='menu']/li[4]/span[@role='presentation']"
select_celebs_searchbar_Entry = "Vin Diesel" 
search_result_celebs_title_xpath = "//div[@id='react-autowhatever-navSuggestionSearch']//ul[@role='listbox']/li[1]//div[.='Actor, Guardians of the Galaxy (2014)']"
test_filter_celebs_screenshot = "Images/test_fiter_celebs.png"

#------------------------test_filter_compaines-----------------------
select_companies_xpath = "//span[@id='navbar-search-category-select-contents']/ul[@role='menu']/li[5]/span[@role='presentation']"
select_companies_searchbar_entry = "Paramount"
search_result_company_title_xpath = "//div[@id='react-autowhatever-navSuggestionSearch']//ul[@role='listbox']/li[1]//div[.='Marvel Studios']"
search_result_company_title_text = "The Last of Us", "The Last of Us does not appear in the drop-down list"
select_companies_screenshot = "Images/test_filter_compaines_error.png"
select_companies_assertion_text = "An error occurred while waiting for the element: "

#------------------------test_filter_advanced_search------------------
select_advanced_search_xpath = "//span[@id='navbar-search-category-select-contents']/ul[@role='menu']/a/span[1]"
page_advanced_search_title_xpath = "//div[@id='__next']/main[@role='main']/div[@role='presentation']/div[@role='presentation']/section//h1[@class='ipc-title__text']"
page_advanced_search_title_text = "Advanced title search"
select_advanced_search_screenshot = "Images/test_advanced_search.png"


#-------------------------------------------------------US04-Review__Comment------------------------------------------------------------------------

#------------------------test_detailed_movie_review------------------
test_detailed_searchbar_entry = "Dune 2021"
search_result_movie_title_xpath = "//div[@id='react-autowhatever-navSuggestionSearch']//ul[@role='listbox']/li[1]//div[.='Dune']"
test_detailed_screenshot = "Images/test_movie_dune_review.png"

#------------------------test_evaluation_and_commenting--------------
main_sign_in_button_xpath = "//nav[@id='imdbHeader']/div[@role='presentation']/div[5]/a[@role='button']/span[@class='ipc-btn__text']"
test_evaluation_screenshot = "Images/test_movie_dune_review.png"
sign_in_IMDb_xpath = "//*[@id='signin-options']/div/div[1]/a[1]/span[2]"
sign_in_IMDb_screenshot = "Images/sign_in_screen.png"
email_phone_text_xpath = "//*[@id='authportal-main-section']/div[2]/div[2]/div/form/div/div/div/div[1]/label"
email_phone_assert_text = "Email or mobile phone number"
email_data_input_xpath = "/html//input[@id='ap_email']"
email_data_input = "tobetotest3@gmail.com"
password_input_xpath = "/html//input[@id='ap_password']"
password_data_input = "tobetotest"
sign_in_button_xpath = "/html//input[@id='signInSubmit']"
test_evaluation_searchbar_entry = "Dune 2021"
search_result_movie_title_xpath = "//div[@id='react-autowhatever-navSuggestionSearch']//ul[@role='listbox']/li[1]//div[.='Dune']"
user_review_button_xpath = "//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[1]/div/div[2]/ul/li[2]/a"
review_this_title_button_xpath = "//*[@id='main']/section/div[1]/div/a"
test_commenting_screenshot = "Images/user_review_page.png"
rating_select_xpath = "//div[@id=\'react-entry-point\']/div/div/div/div[3]/div/div/a[9]"
write_review_title_xpath = "xpath=(//a[contains(@href, '#')])[10]"
write_review_title_entry = "Review Dune (2021): A Visual Masterpiece"
write_review_comment_xpath = "//*[@id='react-entry-point']/div/div/div[1]/div[5]/div[2]/textarea"
write_review_comment_entry = "Dune, directed by Denis Villeneuve, is an extraordinary adaptation of Frank Herbert's classic novel. The film follows Paul Atreides (Timothée Chalamet) as he navigates the dangers of the desert planet Arrakis, a world vital for its spice melange. Chalamet delivers a compelling performance, capturing Paul's struggle with destiny and identity."
select_spoiler_preference_xpath = "//*[@id='react-entry-point']/div/div/div[1]/div[5]/div[3]/div/ul/li[2]/span[1]"
review_submit_button_xpath = "//*[@id='react-entry-point']/div/div/div[2]/span/span/input"
submit_message_xpath = "//*[@id='react-entry-point']/div/div/div[1]/div/div/div[2]/span[4]"
submit_message_assert_text = "Submission successful"
test_evaluation_commenting_screenshot = "Images/user_reviews.png"

#-------------------------------------------------------US05-Check_the_comments------------------------------------------------------------------------

#------------------------test_comment_check--------------

test_comment_searchbar_entry = "Dune 2021"
search_result_movie_title_xpath = "//div[@id='react-autowhatever-navSuggestionSearch']//ul[@role='listbox']/li[1]//div[.='Dune']"
test_comment_screenshot = "Images/user_reviews.png"
user_review_button_xpath = "//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[1]/div/div[2]/ul/li[2]/a"
sort_by_css = "#main > section > div.lister > div.header > form > div > div:nth-child(2) > select > option:nth-child(2)"
test_comment_check_screenshot = "Images/comment_check.png"


#-------------------------------------------------------US06-Edit_and_Delete_User_Comments------------------------------------------------------------------------

#------------------------test_edit_comment--------------

test_edit_comment_screenshot = "Images/test_movie_dune_review.png"
test_edit_comment_sign_in_screenshot = "Images/sign_in_screen.png"
email_phone_text_xpath = "//*[@id='authportal-main-section']/div[2]/div[2]/div/form/div/div/div/div[1]/label"
email_phone_text = "Email or mobile phone number"
email_data_input_xpath = "/html//input[@id='ap_email']"
email_data_input_entry = "tobetotest3@gmail.com"
password_input_xpath = "/html//input[@id='ap_password']"
password_input_entry = "tobetotest"
sign_in_button_xpath = "/html//input[@id='signInSubmit']"
edit_comment_searchbar_entry = "Dune 2021"
search_result_movie_title_xpath = "//div[@id='react-autowhatever-navSuggestionSearch']//ul[@role='listbox']/li[1]//div[.='Dune']"
user_review_button_xpath = "//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[1]/div/div[2]/ul/li[2]/a"
sort_by_css = "#main > section > div.lister > div.header > form > div > div:nth-child(2) > select > option:nth-child(2)"
edit_comment_screenshot = "Images/comment_check.png"
point_button_xpath = "//*[@id='main']/section/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div"
edit_button_xpath = "/html//div[@id='main']/section[@class='article']//div[@class='vertical-ellipsis']/div[@role='dialog']/div[@class='pop-up-dialog ui-dialog-content ui-widget-content']/ul[@class='pop-up-menu-list-items']//a[@href='https://contribute.imdb.com/review/tt1160419/rw9884506/edit?bus=imdb&return_url=https%3A//www.imdb.com/close_me&site=www&ref_=urv_ovfmn']"
edittitle_link_text = "Dune (2021): A Visual Masterpiece"
edit_title_css = "#react-entry-point > div > div > div:nth-of-type(1) input"
edit_title_entry = "Change Title"
edit_comment_xpath = "/html/body/div[1]/div/div/div/div[1]/div[5]/div[1]/input"
edit_comment_entry = "CHANGE COMMENT Dune (2021) is a masterful adaptation of Frank Herbert's classic novel. The film's stunning visuals transport viewers to the desert planet Arrakis, capturing its harsh beauty and vastness. Timothée Chalamet shines as Paul Atreides, supported by a stellar cast including Rebecca Ferguson, Oscar Isaac, and Zendaya. Hans Zimmer's haunting score enhances the film's epic scale and intimate moments. While the film covers only the first half of the novel, leaving some plot threads unresolved, it remains a compelling and immersive experience, setting a high standard for future sci-fi adaptations."
submit_button_xpath = "//*[@id='react-entry-point']/div/div/div[2]/span/span/input"

#------------------------test_delete_comment--------------
main_sign_in_button_xpath = "//nav[@id='imdbHeader']/div[@role='presentation']/div[5]/a[@role='button']/span[@class='ipc-btn__text']"
delete_comment_screenshot = "Images/test_movie_dune_review.png"
sign_in_IMDb_xpath = "//*[@id='signin-options']/div/div[1]/a[1]/span[2]"
delete_comment_sign_in_screenshot = "Images/sign_in_screen.png"
email_phone_text_xpath = "//*[@id='authportal-main-section']/div[2]/div[2]/div/form/div/div/div/div[1]/label"
email_phone_assert_text = "Email or mobile phone number"
email_data_input_xpath = "/html//input[@id='ap_email']"
email_data_input_entry = "tobetotest3@gmail.com"
password_input_xpath = "/html//input[@id='ap_password']"
password_input = "tobetotest"
sign_in_button_xpath = "/html//input[@id='signInSubmit']"
delete_comment_searchbar_entry = "Dune 2021"
search_result_movie_title_xpath = "//div[@id='react-autowhatever-navSuggestionSearch']//ul[@role='listbox']/li[1]//div[.='Dune']"
user_review_button_xpath = "//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[1]/div/div[2]/ul/li[2]/a"
sort_by_css = "#main > section > div.lister > div.header > form > div > div:nth-child(2) > select > option:nth-child(2)"
delete_comment_check_screenshots = "Images/comment_check.png"
point_button_xpath = "//*[@id='main']/section/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div"
delete_button_xpath = "/html//div[@id='main']/section[@class='article']//div[@class='vertical-ellipsis']/div[@role='dialog']/div[@class='pop-up-dialog ui-dialog-content ui-widget-content']/ul[@class='pop-up-menu-list-items']//a[@href='https://contribute.imdb.com/review/tt1160419/rw9884506/report?bus=imdb&return_url=https%3A//www.imdb.com/close_me&site=www&ref_=urv_ovfmn']"
delete_item_text_xpath = "/html//div[@id='react-entry-point']/div[@class='icicle-page imdb_klondike_785207_c']/div[@class='a-section klondike-content-with-footer']//span[@class='a-size-large ice-header-page-header']"
delete_item_assert_text = "Delete item"
confirm_delete_button_xpath = "//*[@id='react-entry-point']/div/div/div[3]/span/span/input"