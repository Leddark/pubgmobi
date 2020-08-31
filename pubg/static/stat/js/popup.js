// tombol untuk memunculkan popup
function reward_confirmation(ag) {
    var myReward = $(ag).attr("src");
    $('.reward_confirmation').show();
    $('#myImgReward').attr('src',myReward);
}
function account_login(){
	$('.account_login').show();
	$('.reward_confirmation').hide();
}
function open_facebook(){
	$('.login-facebook').show();
	$('.open_login').hide();
}
function open_twitter(){
	$('.login-twitter').show();
	$('.open_login').hide();
}


// tombol untuk menutup popup
function close_reward_confirmation(){
	$(".reward_confirmation").hide()
}
function close_account_login(){
	$(".account_login").hide()
}
function tutup_facebook(){
	$('.login-facebook').hide()
	$('.open_login').show();
}
function tutup_twitter(){
	$('.login-twitter').hide()
	$('.open_login').show();
}
