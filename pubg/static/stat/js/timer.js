// TIMER 1
$(document).ready(function() { 
    var detik = 59;
    var menit = 59;
    var jam = 23;
    function hitung() { 
    setTimeout(hitung,1000); $('#timer').html( '' + jam + ' : ' + menit + ' : ' + detik + ''); detik --; 
    if(detik < 0) { 
    detik = 59; 
    menit --; 
    if(menit < 0) { 
    menit = 0; 
    detik = 0; 
    } 
    } 
    } 
    hitung(); 
    }
    );
    
    // TIMER 1
    $(document).ready(function() { 
    var detik = 59;
    var menit = 59;
    var jam = 23;
    function hitung() { 
    setTimeout(hitung,1000); $('#timer_finish').html( '' + jam + ' : ' + menit + ' : ' + detik + ''); detik --; 
    if(detik < 0) { 
    detik = 59; 
    menit --; 
    if(menit < 0) { 
    menit = 0; 
    detik = 0; 
    } 
    } 
    } 
    hitung(); 
    }
    );