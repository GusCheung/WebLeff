;
(function($) {
    //默认值
    var defaultOptions = {};

    var def_item_opiton = {
        closable: true,
        selected: false,
        icon: "",
        content: ""
    };

    var TABSHTML_STATIC = '<div class="tabs-header"><span class="tab-scroll-left"></span><span class="tab-scroll-right"></span><div class="tabs-wrapper"> <ul></ul></div></div><div class="tabs-panels"></div>';
    var TABSITEM_STATIC = '<li data="{{data}}" name="{{name}}"><div><span class="{{iconClass}}"></span>{{title}}<span class="{{closeClass}}"></span></div></li>';
    var PANEL_STATIC = '<div class="tabs-panel" id="{{id}}"></div>';

    function close_one(ele,container) {
        //debugger;
        var item = $(ele).parents("li");
        var panel_id = item.attr("data");
        var panel = container.find(".tabs-panels>#" + panel_id);
        var prev_item = item.prev("li");
        var next_item = item.next("li");
        if (item.hasClass("selected")) {
            if (prev_item.length > 0) {
                prev_item.click();
            } else if (next_item.length > 0) {
                next_item.click();
            }
        }
        item.remove();
        panel.remove();
    }
    function exist_tab(target, title) {
        var item = target.find(".tabs-wrapper>ul>li[name='" + title + "']");
        if (item.length > 0)
            return true;
        return false;
    }
    function add_item(target, item_options) {
        var index = target.find(".tabs-wrapper>ul>li").length;
        
        if (item_options.title) {
            if (exist_tab(target, item_options.title)) {
                target.find(".tabs-wrapper>ul>li[name='" + item_options.title + "']").click();
                return;
            }
            var item = $(TABSITEM_STATIC.replace(/{{data}}/g, index + "_panel")
                .replace(/{{iconClass}}/g, "icon " + item_options.icon)
                .replace(/{{name}}/g, item_options.title)
                .replace(/{{title}}/g, item_options.title)
                .replace(/{{closeClass}}/g, item_options.closable ? "tab_close" : ""));
            item.click(function() {
                target.find(".tabs-wrapper>ul>li").removeClass("selected");
                target.find(".tabs-panels>.tabs-panel").removeClass("selected-panel");
                $(this).addClass("selected");
                var panel_id = $(this).attr("data");
                
                target.find(".tabs-panels>#" + panel_id).addClass("selected-panel");
            });
            item.bind("contextmenu", function(e) {
                var li = $(e.target).closest("li");
                return false;
            });
            var close_btn = item.find(".tab_close");
            if (close_btn)
                close_btn.click(function() {
                    close_one(this,target);
                });
            var panel = $(PANEL_STATIC.replace(/{{id}}/g, index + "_panel"));
            panel.append(item_options.content);
            target.find(".tabs-wrapper>ul").append(item);
            target.find(".tabs-panels").append(panel);
            if (item_options.selected)
                item.click();
        } else {
            console.log("title参数不存在");
        }
    }

    function contextmenu_li(ele) {

    }

    function Tabs(options, ele) {
        this.$target = ele;
        this.config = $.extend({}, defaultOptions, options);
        this.init();
    }

    $.extend(Tabs.prototype, {
        init: function() {
            // this.state_machine = new StateMachine;
            this.$target.addClass('tabs-container');
            this.$target.append(TABSHTML_STATIC);

        }
    });
    $.fn.iTabs = function(method, options) {
        if (typeof method == "string") {
            return $.fn.iTabs.methods[method](this, options);
        }
        return this.each(function() {
            new Tabs(options, $(this));
        });
    };
    $.fn.iTabs.methods = {
        add: function(target, item_options) {
            item_options = $.extend(def_item_opiton, item_options);
            add_item(target, item_options);
        }
    };

})(jQuery);