(function(t){function e(e){for(var s,o,r=e[0],c=e[1],l=e[2],d=0,v=[];d<r.length;d++)o=r[d],Object.prototype.hasOwnProperty.call(a,o)&&a[o]&&v.push(a[o][0]),a[o]=0;for(s in c)Object.prototype.hasOwnProperty.call(c,s)&&(t[s]=c[s]);u&&u(e);while(v.length)v.shift()();return n.push.apply(n,l||[]),i()}function i(){for(var t,e=0;e<n.length;e++){for(var i=n[e],s=!0,r=1;r<i.length;r++){var c=i[r];0!==a[c]&&(s=!1)}s&&(n.splice(e--,1),t=o(o.s=i[0]))}return t}var s={},a={index:0},n=[];function o(e){if(s[e])return s[e].exports;var i=s[e]={i:e,l:!1,exports:{}};return t[e].call(i.exports,i,i.exports,o),i.l=!0,i.exports}o.m=t,o.c=s,o.d=function(t,e,i){o.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:i})},o.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},o.t=function(t,e){if(1&e&&(t=o(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var i=Object.create(null);if(o.r(i),Object.defineProperty(i,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var s in t)o.d(i,s,function(e){return t[e]}.bind(null,s));return i},o.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return o.d(e,"a",e),e},o.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},o.p="/static/bundles/";var r=window["webpackJsonp"]=window["webpackJsonp"]||[],c=r.push.bind(r);r.push=e,r=r.slice();for(var l=0;l<r.length;l++)e(r[l]);var u=c;n.push([1,"chunk-vendors"]),i()})({1:function(t,e,i){t.exports=i("b635")},"26b8":function(t,e,i){"use strict";i("c214")},3201:function(t,e,i){},"360c":function(t,e,i){},4412:function(t,e,i){},"50b9":function(t,e,i){"use strict";i("f671")},"5f9a":function(t,e,i){"use strict";i("360c")},6846:function(t,e,i){"use strict";i("3201")},"70d5":function(t,e,i){"use strict";i("cb73")},b635:function(t,e,i){"use strict";i.r(e);i("e260"),i("e6cf"),i("cca6"),i("a79d");var s=i("a026"),a=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{attrs:{id:"main"}},[i("div",{attrs:{id:"grid"}},[i("div",{staticClass:"container"},[i("div",{staticClass:"filters"},[i("div",{staticClass:"columns"},[i("div",{staticClass:"column checkbox-list"},[i("b-field",{staticClass:"is-grouped",attrs:{label:t.$t("index.view")}},[i("b-checkbox",{attrs:{"native-value":"creative",disabled:"creative"==t.viewType},on:{input:t.setViewType},model:{value:t.viewType,callback:function(e){t.viewType=e},expression:"viewType"}},[t._v(" "+t._s(t.$t("index.creatives"))+" ")]),i("b-checkbox",{attrs:{"native-value":"group",disabled:"group"==t.viewType},on:{input:t.setViewType},model:{value:t.viewType,callback:function(e){t.viewType=e},expression:"viewType"}},[t._v(" "+t._s(t.$t("index.groups"))+" ")])],1)],1),i("div",{staticClass:"column is-narrow is-hidden-mobile"},[i("b-field",{staticClass:"is-grouped",attrs:{label:t.$t("index.sort.label")}},[i("b-select",{on:{input:t.orderBy},model:{value:t.sort.active,callback:function(e){t.$set(t.sort,"active",e)},expression:"sort.active"}},t._l(t.sort.options,(function(e,s){return i("option",{key:s,domProps:{value:s,textContent:t._s(e.label)}})})),0)],1)],1)])])]),i("GridHead",{staticClass:"container",attrs:{active:t.active,favorites:t.favorites.length,tags:t.searchTags,isLoading:t.loading.search,counters:{sector:t.getCount(t.active.sector),category:t.getCount(t.active.category)}},on:{search:t.search,"view-categories":function(e){return t.loadCategories(t.active.sector)},"view-all":function(e){return t.restart()},fav:function(e){return t.loadFavorites()}}}),i("div",{staticClass:"container entities"},[i("TransitionHeight",[t.active.entities&&t.active.entities.length?i("div",{key:"entities-"+t.active.entities.length+(t.sort.active<3?t.sort.active:"")},[i("div",{staticClass:"masonry"},[t._l(t.active.entities,(function(e,s){return i("EntityBox",t._b({key:s,attrs:{searching:null!=t.active.search},on:{click:function(i){return t.loadProfile(e,t.active.entities)}}},"EntityBox",{entity:e,index:s},!1))})),t._l(t.filler.entities,(function(e,s){return i("EntityBox",{key:"e-"+s,attrs:{rowspan:e,index:s+t.active.entities.length,searching:null!=t.active.search}})}))],2)]):t._e()])],1),i("div",{staticClass:"container categories"},[i("TransitionExpand",[t.active.sector&&!t.active.search?i("div",{key:"categories-"+t.active.sector.id+"-sort-"+t.sort.active+t.viewType.length},[i("div",{staticClass:"masonry has-space-bottom"},[t._l(t.active.sector.categories,(function(e,s){return i("Box",{key:e.id,attrs:{name:e.name,counter:t.getCount(e),rowspan:e.rowspan,color:t.active.sector.color,colorActive:t.active.sector.color_active,index:s,isActive:e==t.active.category,boxType:"category"},on:{click:function(i){return t.loadEntities(e)}}})})),t._l(t.filler.categories,(function(e,s){return i("Box",{key:"f-"+s,attrs:{rowspan:e,index:s+t.active.sector.categories.length}})}))],2)]):t._e()])],1),i("div",{staticClass:"container sectors"},[i("TransitionExpand",[i("div",{key:"sectors-sort-"+t.sort.active+t.viewType.length},[t.sectors.length?t._e():i("div",{staticClass:"button is-clear is-fullwidth grid-loading",class:{"is-loading":!0}}),i("div",{staticClass:"masonry has-space-bottom"},[t._l(t.sectors,(function(e,s){return i("Box",{key:e.id,attrs:{name:e.name,counter:t.getCount(e),rowspan:e.rowspan,color:e.color,colorActive:e.color_active,index:s,isActive:e==t.active.sector,boxType:"sector"},on:{click:function(i){return t.loadCategories(e)}}})})),t._l(t.filler.sectors,(function(e,s){return i("Box",{key:"f-"+s,attrs:{rowspan:e,index:s+t.sectors.length}})}))],2)])])],1)],1)])},n=[],o=(i("99af"),i("cb29"),i("4de4"),i("7db0"),i("4160"),i("c975"),i("d81d"),i("13d5"),i("b0c0"),i("ac1f"),i("841c"),i("159b"),i("d7c2")),r=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("transition",{attrs:{name:"grow",appear:""}},[i("div",{staticClass:"wrapper",style:{"grid-row-end":"span "+t.rowspan,"transition-delay":30*t.index+"ms"}},[i("div",{staticClass:"button is-box",class:{"is-empty":!t.name||!t.name.length},style:{"background-color":t.isDisabled?null:t.isActive?t.colorActive:t.color},attrs:{disabled:t.isDisabled},on:{click:function(e){!t.isDisabled&&t.$emit("click")}}},[i("b",[t._v(t._s(t.name))]),t.isDisabled?t._e():i("div",{staticClass:"counter"},[t._v(t._s(t.counter))])])])])},c=[],l=(i("a9e3"),{name:"Box",props:{name:String,color:String,colorActive:String,counter:Number,rowspan:Number,index:Number,isActive:Boolean,boxType:String},computed:{isDisabled:function(){return 0===this.counter&&"category"==this.boxType}}}),u=l,d=(i("50b9"),i("2877")),v=Object(d["a"])(u,r,c,!1,null,"3d9be68a",null),f=v.exports,h=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("transition",{attrs:{name:"grow",appear:""}},[i("div",{staticClass:"wrapper entity-box",style:{"grid-row-end":t.searching&&(t.rowspan||t.entity)?t.getRowspan():null,"transition-delay":30*t.index+"ms"}},[i("div",{staticClass:"button is-box",class:{"is-empty":!t.entity},on:{click:function(e){return t.$emit("click")}}},[t.entity?[i("div",{staticClass:"info"},[t.entity.profile_picture?i("img",{attrs:{src:decodeURIComponent(t.entity.profile_picture),alt:t.entity.name}}):i("div",{staticClass:"placeholder"},[i("b-icon",{attrs:{icon:"person"}})],1),i("div",[i("b",{domProps:{textContent:t._s(t.entity.name)}}),t.entity.title||t.entity.role?i("p",{staticClass:"subtitle is-size-7 has-text-grey-lighter",domProps:{textContent:t._s(t.entity.title||t.entity.role)}}):t._e()])]),t.searching?i("div",{staticClass:"search-results"},[t.entity.interests.length?i("div",{staticClass:"result"},[i("div",{staticClass:"label-text has-text-grey-lighter"},[t._v(t._s(t.$t("index.interests")))]),i("div",{staticClass:"enumeration"},[t._v(" "+t._s(t.trunc(t.entity.interests))+" ")])]):t._e(),t.entity.categories.length?i("div",{staticClass:"result"},[i("div",{staticClass:"label-text has-text-grey-lighter"},[t._v(t._s(t.$t("index.category")))]),i("div",{staticClass:"enumeration"},[t._v(" "+t._s(t.trunc(t.entity.categories))+" ")])]):t._e(),t.entity.sectors.length?i("div",{staticClass:"result"},[i("div",{staticClass:"label-text has-text-grey-lighter"},[t._v(t._s(t.$t("index.sector")))]),i("div",{staticClass:"enumeration"},[t._v(" "+t._s(t.trunc(t.entity.sectors))+" ")])]):t._e()]):t._e(),"group"==t.entity.type?i("b-icon",{staticClass:"is-size-6 has-text-grey-lighter is-label",attrs:{icon:"people"}}):t._e()]:t._e()],2)])])},p=[],m=(i("a15b"),{name:"EntityBox",props:{entity:Object,index:Number,searching:null,rowspan:null},methods:{getRowspan:function(){return"span "+(this.rowspan?this.rowspan:this.entity.rowspan)},trunc:function(t){var e=t.join(", "),i=26;return e.length>i?e.substr(0,i-1)+"...":e}}}),g=m,y=(i("f9e8"),Object(d["a"])(g,h,p,!1,null,"64a2b678",null)),b=y.exports,_=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{ref:"modal",staticClass:"modal-body",attrs:{id:"entityProfile"}},[i("b-loading",{attrs:{"is-full-page":!1,active:t.isLoading.modal}}),i("b-button",{staticClass:"modal-close-custom is-clear",attrs:{iconLeft:"close"},on:{click:function(e){return t.$emit("close")}}}),t.nextProfile?i("b-button",{staticClass:"modal-nav next",attrs:{disabled:t.isLoading.modal},on:{click:function(e){return t.loadProfile(t.nextProfile.url)}}},[i("b-icon",{attrs:{icon:"arrow-round-forward"}})],1):t._e(),t.prevProfile?i("b-button",{staticClass:"modal-nav prev",attrs:{disabled:t.isLoading.modal},on:{click:function(e){return t.loadProfile(t.prevProfile.url)}}},[i("b-icon",{attrs:{icon:"arrow-round-back"}})],1):t._e(),t.model?i("div",{staticClass:"columns"},[i("div",{staticClass:"column is-4 column-side"},[i("div",{staticClass:"profile-card"},[i("div",{staticClass:"image"},[t.model.profile_picture?i("img",{staticClass:"img-responsive",attrs:{src:decodeURIComponent(t.model.profile_picture)}}):t._e()]),i("div",[i("h1",{staticClass:"title is-size-5"},[i("b",[t._v(t._s(t.model.name))])]),i("div",{staticClass:"subtitle has-text-grey-lighter is-size-7"},[t.model.ocupation?i("p",[t._v(t._s(t.model.ocupation))]):t._e(),t.model.organization?i("p",[t._v(t._s(t.model.organization))]):t._e(),t.model.title?i("p",[t._v(t._s(t.model.title))]):t._e()])])]),i("div",{staticClass:"is-hidden-tablet"},[i("div",{staticClass:"profile-head is-size-7"},[i("div",{staticClass:"item"},[t._v(" "+t._s(t.$t("index.creative_profile"))+" ")])]),t.model.links&&t.model.links.length?i("div",{staticClass:"buttons has-addons"},t._l(t.model.links,(function(e,s){return i("a",{key:"link"+s,staticClass:"button is-size-7",attrs:{href:e.url,target:"_blank"}},[t._v(" "+t._s(e.platform)+" ")])})),0):t._e()]),i("ul",{staticClass:"tag-list is-vertical"},t._l(t.model.categories,(function(e,s){return i("li",{key:"cat-"+s,staticClass:"category"},[i("button",{staticClass:"tag button",style:{"border-color":e.color,color:e.color},on:{click:function(i){return t.$emit("changeCategory",e)}}},[i("div",{staticClass:"boop",style:{"background-color":e.color}}),t._v(" "+t._s(e.name)+" ")])])})),0),i("b-field",{staticClass:"field-fav"},[i("b-button",{staticClass:"is-clear is-size-7 star",attrs:{"icon-left":t.fav.active?"star":"star-outline",loading:t.isLoading.fav,disabled:t.isLoading.fav},on:{click:t.toggleFav}}),i("b-button",{staticClass:"is-clear is-size-7",attrs:{disabled:t.isLoading.fav},on:{click:t.toggleFav}},[t._v(" "+t._s(t.fav.active?t.$t("index.fav_remove"):t.$t("index.fav_add"))+" "+t._s(t.$t("index.fav"))+" ")])],1)],1),i("div",{staticClass:"column"},[i("div",{staticClass:"profile-head is-size-7 is-hidden-mobile"},["creative"==t.model.type?i("div",{staticClass:"item"},[t._v(" "+t._s(t.$t("index.creative_profile"))+" ")]):i("div",{staticClass:"item"},[t._v(" "+t._s(t.$t("index.group_profile"))+" ")])]),t.model.links&&t.model.links.length?i("div",{staticClass:"buttons has-addons is-hidden-mobile"},t._l(t.model.links,(function(e,s){return i("a",{key:"link"+s,staticClass:"button is-size-7",attrs:{href:e.url,target:"_blank"}},[t._v(t._s(e.platform))])})),0):t._e(),i("div",{staticClass:"bio is-size-7-touch"},[t._v(t._s(t.clean(t.model.bio)))]),t.model.active_groups&&t.model.active_groups.length?i("div",[i("p",{staticClass:"label has-text-grey-lighter is-size-7"},[t._v(" "+t._s(t.$t("index.member_of"))+" ")]),i("div",{staticClass:"columns is-multiline"},t._l(t.model.active_groups,(function(e){return i("div",{key:e.slug,staticClass:"column is-6"},[i("EntityBox",{attrs:{entity:Object.assign({},e,{type:"group"})},on:{click:function(i){return t.loadProfile(e.url)}}})],1)})),0)]):t._e(),t.model.members&&t.model.members.length?i("div",[i("p",{staticClass:"label has-text-grey-lighter is-size-7",domProps:{textContent:t._s(t.$t("index.members")+" ("+t.model.members.length+")")}}),i("div",{staticClass:"columns is-multiline"},t._l(t.model.members,(function(e){return i("div",{key:e.slug,staticClass:"column is-6"},[i("EntityBox",{attrs:{entity:e},on:{click:function(i){return t.loadProfile(e.url)}}})],1)})),0)]):t._e(),i("div",{staticClass:"tag-list is-horizontal has-text-grey-lighter"},[i("p",{staticClass:"label has-text-grey-lighter is-size-7"},[t._v(" "+t._s(t.$t("index.interests"))+" ")]),t._l(t.model.interests,(function(e,s){return i("div",{key:"int"+s,staticClass:"interest tag"},[t._v(" "+t._s(e)+" ")])}))],2)])]):t._e()],1)},C=[],w=(i("c740"),i("a434"),i("5319"),i("498a"),i("2909")),x=i("5530"),k={name:"EntityProfile",components:{EntityBox:b},props:{entity:Object,entityList:Array,favorites:Array,is_anonymous:Boolean},data:function(){return{model:null,fav:{active:null,index:null},isLoading:{fav:!1,modal:!1},nextProfile:null,prevProfile:null,keyListener:null}},mounted:function(){this.initKeyNav(),this.loadProfile(this.entity.url)},beforeDestroy:function(){document.removeEventListener("keydown",this.keyListener)},methods:{initKeyNav:function(){var t=this;this.keyListener=function(e){t.isLoading.modal||(37===e.keyCode&&t.prevProfile?t.loadProfile(t.prevProfile.url):39===e.keyCode&&t.nextProfile&&t.loadProfile(t.nextProfile.url))},document.addEventListener("keydown",this.keyListener)},getEntityIndex:function(t){var e=this;return t.findIndex((function(t){return t.type==e.model.type&&t.id==e.model.id}))},getNavProfile:function(t){var e=this.getEntityIndex(this.entityList);return-1!=e&&(t>0&&e<this.entityList.length-1||t<0&&e>0)?this.entityList[e+t]:null},loadProfile:function(t){var e=this;t&&(this.isLoading.modal=!0,Object(o["b"])(t,{},!0).then((function(i){e.model=Object(x["a"])(Object(x["a"])({},i),{},{url:t}),e.isLoading.modal=!1,e.fav.index=e.getEntityIndex(e.favorites),e.fav.active=-1!=e.fav.index,e.nextProfile=e.getNavProfile(1),e.prevProfile=e.getNavProfile(-1),e.$emit("setHash",{slug:e.model.slug,type:e.model.type})})).catch((function(){e.isLoading.modal=!1})))},toggleFav:function(){var t=this;if(this.is_anonymous)this.$buefy.snackbar.open({message:this.$t("index.fav_error"),actionText:this.$t("login"),type:"is-black",position:"is-top",duration:5e3,onAction:function(){window.location="/login"}});else{this.isLoading.fav=!0;var e=Object(w["a"])(this.favorites);this.fav.active?e.splice(this.fav.index,1):e.push({id:this.model.id,name:this.model.name,profile_picture:this.model.profile_picture,slug:this.model.slug,type:this.model.type,url:this.model.url});var i=function(t){return e.filter((function(e){return e.type==t})).map((function(t){return t.id}))},s={favorites:{groups:i("group"),creatives:i("creative")}};Object(o["b"])("favorites",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(s)}).then((function(i){t.isLoading.fav=!1,null!=i.success&&(t.$emit("fav",e),t.fav.active=!t.fav.active,t.fav.index=e.length-1)})).catch((function(){t.isLoading.fav=!1}))}},clean:function(t){return t&&t.trim().replace(/(\n )/g,"\n")}}},T=k,P=(i("26b8"),i("6846"),Object(d["a"])(T,_,C,!1,null,"724aedbf",null)),$=P.exports,E=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{attrs:{id:"gridHead"}},[i("div",{staticClass:"columns is-mobile"},[i("div",{staticClass:"column"},[i("div",{staticClass:"field has-background-grey-darker has-addons search-field"},[i("div",{staticClass:"button",class:{"is-loading":t.isLoading}},[i("b-icon",{staticClass:"is-size-5 has-text-grey",attrs:{icon:"arrow-forward"}})],1),i("b-taginput",{ref:"searchtags",attrs:{placeholder:t.$t("index.search"),maxlength:"20",maxtags:"7","has-counter":!1},on:{input:t.updateTags},model:{value:t.searchTags,callback:function(e){t.searchTags=e},expression:"searchTags"}},[i("template",{slot:"selected"},[i("span")])],2)],1)]),i("div",{staticClass:"column is-narrow"},[i("button",{staticClass:"button has-text-white spaced-between",class:{"is-active":t.active.favorites},attrs:{type:"button"},on:{click:function(e){t.favorites&&!t.active.favorites&&t.$emit("fav")}}},[i("div",[i("b-icon",{attrs:{icon:"star"}}),i("b",{staticClass:"is-hidden-mobile"},[t._v(" "+t._s(t.$t("index.fav"))+" ")])],1),i("span",{staticClass:"counter"},[t._v(t._s(t.favorites?t.favorites:"0"))])])])]),i("TransitionExpand",[t.active.sector||t.active.favorites||t.active.search?i("div",{staticClass:"wrapper"},[i("div",{staticClass:"columns navigation is-mobile is-multiline"},[i("div",{staticClass:"column is-narrow",class:{"view-all":t.active.search}},[i("button",{staticClass:"button",on:{click:function(e){return t.$emit("view-all")}}},[i("b",[t._v(t._s(t.$t("index.all")))])])]),t.active.favorites?i("div",{staticClass:"column"},[i("button",{staticClass:"button spaced-between",attrs:{type:"button"}},[i("b",[t._v(t._s(t.$t("index.fav")))])])]):t._e(),t.active.search?i("div",{staticClass:"column"},[i("div",{staticClass:"search-bar"},[t._l(t.searchTags,(function(e,s){return i("b-tag",{key:"tag-"+s,attrs:{closable:!0},on:{close:function(e){return t.$refs.searchtags.removeTag(s,e)}}},[t._t("tag",[t._v(" "+t._s(e)+" ")],{tag:e})],2)})),i("a",{on:{click:function(e){return t.$emit("view-all")}}},[t._v(t._s(t.$t("index.delete_filters")))])],2)]):t._e(),t.active.sector?i("div",{staticClass:"column"},[i("button",{staticClass:"button spaced-between",style:{"background-color":t.active.sector.color},attrs:{type:"button"},on:{click:function(e){return t.$emit("view-categories")}}},[i("b",[t._v(t._s(t.active.sector.name))]),i("span",{staticClass:"counter"},[t._v(t._s(t.counters.sector))])])]):t._e(),t.active.category?i("div",{staticClass:"column is-12-mobile"},[i("button",{staticClass:"button spaced-between",style:{"background-color":t.active.sector.color_active},attrs:{type:"button"}},[i("b",[t._v(t._s(t.active.category.name))]),i("span",{staticClass:"counter"},[t._v(t._s(t.counters.category))])])]):t._e()])]):t._e()])],1)},S=[],L=(i("fb6a"),function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("transition",{attrs:{name:"expand",appear:""},on:{enter:t.enter,"after-enter":t.afterEnter,leave:t.leave}},[t._t("default")],2)}),z=[],A={name:"TransitionExpand",methods:{enter:function(t){t.style.height="auto";var e=getComputedStyle(t).height;t.style.height=0,getComputedStyle(t).height,setTimeout((function(){t.style.height=e}))},afterEnter:function(t){t.style.height="auto"},leave:function(t){var e=getComputedStyle(t).height;t.style.height=e,getComputedStyle(t).height,setTimeout((function(){t.style.height=0}))}}},O=A,j=Object(d["a"])(O,L,z,!1,null,"f3eec592",null),G=j.exports,I={name:"GridHead",components:{TransitionExpand:G},data:function(){return{sortActive:1,searchTags:[]}},props:{tags:Array,active:Object,favorites:Number,isLoading:Boolean,counters:Object},watch:{tags:function(t){this.searchTags=t.slice()}},methods:{updateTags:function(t){this.$emit("search",t)}}},N=I,F=(i("70d5"),Object(d["a"])(N,E,S,!1,null,null,null)),B=F.exports,H=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("transition",{attrs:{name:"expand",appear:""},on:{enter:t.enter,"after-enter":t.afterEnter,leave:t.leave}},[t._t("default")],2)},R=[],M={name:"TransitionExpand",data:function(){return{prevHeight:0}},methods:{enter:function(t){this.$nextTick((function(){var e=getComputedStyle(t).width;t.style.width=e,t.style.position="absolute",t.style.visibility="hidden",t.style.height="auto",t.parentNode.style.height=this.prevHeight,t.style.height="auto";var i=getComputedStyle(t).height;t.style.width=null,t.style.position=null,t.style.visibility=null,setTimeout((function(){t.parentNode.style.height=i}),0)}))},afterEnter:function(t){t.style.height="auto"},leave:function(t){var e=this,i=getComputedStyle(t).width;t.style.width=i,t.style.position="absolute",t.style.visibility="hidden";var s=getComputedStyle(t).height;t.style.height=s,getComputedStyle(t).height,setTimeout((function(){t.parentNode.style.height=e.prevHeight}),0)}}},V=M,q=Object(d["a"])(V,H,R,!1,null,"10fbc7ec",null),D=q.exports,U={name:"app",components:{Box:f,EntityBox:b,GridHead:B,TransitionExpand:G,TransitionHeight:D},data:function(){return{sectors:[],favorites:[],viewType:["creative","group"],is_anonymous:!0,searchTags:[],sort:{active:0,options:[{label:this.$t("index.sort.atoz"),type:"name",direction:1},{label:this.$t("index.sort.ztoa"),type:"name",direction:-1},{label:this.$t("index.sort.numasc"),type:"number",direction:1},{label:this.$t("index.sort.numdesc"),type:"number",direction:-1}]},stats:"",filler:{sectors:[],categories:[],entities:[]},active:{sector:null,category:null,creative:null,entities:null,search:null,favorites:!1,stats:""},loading:{grid:!1,fav:!1,search:!1},logoElement:null,modalInstance:null}},mounted:function(){var t=this;this.logoElement=document.getElementById("logo-svg"),window.addEventListener("DOMContentLoaded",(function(){t.init()}))},methods:{init:function(){var t=this;this.loading.grid=!0,Object(o["b"])("grid-data").then((function(e){t.sectors=e.sectors,t.favorites=e.favorites,t.is_anonymous=e.is_anonymous,t.loading.grid=!1,t.computeRowSpans(),t.orderBy();var i=e.notifications;i&&i.length&&setTimeout((function(){i.forEach((function(e){t.$buefy.snackbar.open({message:e.message,duration:e.duration,indefinite:null==e.duration,position:"is-top",type:"is-black",actionText:e.action_text,onAction:function(){null!=e.action&&(window.location=e.action)}})}))}),2e3),t.initURL()}))},initURL:function(){var t=window.APP.init;if(!isNaN(t.sector)){var e=this.sectors.find((function(e){return e.id==t.sector}));if(null!=e&&(this.loadCategories(e,!0),!isNaN(t.category))){var i=e.categories.find((function(e){return e.id==t.category}));null!=i&&(this.loadEntities(i,!0),t.entity.url.length&&"None"!=t.entity.url&&this.loadProfile(t.entity,this.active.entities))}}},computeRowSpans:function(){var t=this;if(this.sectors.length){var e="sm"==this.$mq?80:120,i="sm"==this.$mq?120:300,s=6,a=function(t){return Math.round(((i-e)*t/100+e)/s+1)},n=function(e){return t.viewType.length>1?e.stats["creative"].p:e.stats[t.viewType[0]].p};this.sectors.map((function(t){t.rowspan=a(n(t)),t.categories.map((function(t){t.rowspan=a(n(t))}))}))}},computeSearchRowSpans:function(){var t=function(t){var e=0;return t.sectors.length&&e++,t.categories.length&&e++,t.interests.length&&e++,15+4*e};this.active.entities.map((function(e){e.rowspan=t(e)}))},computeGridFills:function(t,e){if(t&&t.length){for(var i={sm:2,md:3,lg:4,xl:5}[this.$mq],s=Array(i).fill(0),a=function(t){for(var e=t[0],i=0,s=1;s<t.length;s++)e>t[s]&&(i=s,e=t[s]);return i},n=0;n<t.length;n++)s[a(s)]+=t[n].rowspan;s.sort((function(t,e){return t-e}));var o=s[s.length-1]+("sm"!=this.$mq?21:11);this.filler[e]=[];for(var r=0;r<i;r++)this.filler[e].push(o-s[r])}},computeGridFillsEntities:function(){if(this.active.entities){var t={sm:2,md:3,lg:4,xl:5}[this.$mq];this.filler.entities=Array(t-this.active.entities.length%t)}},computeGridSizes:function(){this.computeRowSpans(),this.computeGridFills(this.sectors,"sectors"),this.active.sector&&this.computeGridFills(this.active.sector.categories,"categories"),!this.active.search&&this.computeGridFillsEntities()},orderBy:function(){var t,e=this,i=!1,s=this.sort.options[this.sort.active],a=s.type,n=s.direction;switch(a){case"name":t=function(t,e){return t.name<e.name?-n:t.name>e.name?n:0},i=!0;break;case"number":t=function(t,i){return e.getCount(t)<e.getCount(i)?-n:e.getCount(t)>e.getCount(i)?n:0};break;default:return}this.sectors.sort(t),this.sectors.map((function(e){e.categories.sort(t),i&&e.categories.map((function(e){return e.entities.sort(t)}))})),i&&this.favorites.sort(t),i&&this.active.entities&&this.active.entities.sort(t),this.computeGridFills(this.sectors,"sectors"),this.active.sector&&this.computeGridFills(this.active.sector.categories,"categories")},search:function(t){var e=this;t.length?(this.loading.search=!0,this.setHash(!0),Object(o["b"])("search/?q="+t).then((function(t){e.restart(!0),e.loading.search=!1,e.active.search=t.results,e.loadSearch()}))):this.restart()},restart:function(t){this.active={sector:null,category:null,creative:null,favorites:!1,stats:this.stats},this.scrollTop(),this.setLogoColor(),this.setHash(!0),t||(this.searchTags=[],this.active.search=null)},setLogoColor:function(){this.logoElement.style.fill=null!=this.active.sector?this.active.sector.color:""},loadCategories:function(t,e){this.active={sector:t,stats:t.stats,category:null,search:null,favorites:!1},this.searchTags=[],this.computeGridFills(this.active.sector.categories,"categories"),this.setLogoColor(),e||(this.scrollTop(),this.setHash())},loadCategoryById:function(t){this.active.search=null,this.searchTags=[],this.active.favorites=!1,this.active.sector=this.sectors.find((function(e){return e.id===t.sector_id})),this.active.category=this.active.sector.categories.find((function(e){return e.id===t.id})),this.active.entities=this.filterViewType(this.active.category.entities),this.computeGridFills(this.active.sector.categories,"categories"),this.computeGridFillsEntities(),this.setLogoColor(),this.scrollTop(),this.setHash()},loadEntities:function(t,e){this.active.category=t,this.active.entities=this.filterViewType(t.entities),this.active.favorites=!1,this.computeGridFillsEntities(),this.setLogoColor(),e||(this.scrollTop(),this.setHash())},loadProfile:function(t,e){var i=this;t.url&&(this.modalInstance=this.$buefy.modal.open({animation:null,parent:this,component:$,props:{entity:t,entityList:e,favorites:this.favorites,is_anonymous:this.is_anonymous},width:960,events:{setHash:function(t){i.setHash(!1,t)},changeCategory:function(t){i.modalInstance.close(),i.loadCategoryById(t)},fav:this.updateFav},onCancel:function(){i.setHash()}}))},updateFav:function(t){this.favorites=t,this.modalInstance&&(this.modalInstance.props["favorites"]=this.favorites,this.modalInstance.$forceUpdate()),this.active.favorites&&(this.active.entities=this.filterViewType(this.favorites),this.computeGridFillsEntities())},loadFavorites:function(){this.restart(),this.active.entities=this.filterViewType(this.favorites),this.active.favorites=!0,this.computeGridFillsEntities()},loadSearch:function(){this.active.entities=this.filterViewType(this.active.search),this.computeSearchRowSpans(),this.computeGridFills(this.active.entities,"entities")},scrollTop:function(){"sm"!=this.$mq?this.$scrollTo("body"):this.$scrollTo("#stats",500,{offset:-20})},setHash:function(t,e){var i="/".concat(window.APP.lang,"/");t||(this.active.sector?(i+="grid/"+this.active.sector.slug,this.active.category&&(i+="/"+this.active.category.slug,e&&e.slug&&(i+="/".concat(e.type,"/").concat(e.slug)))):e&&e.slug&&(i+="profile/".concat(e.type,"/").concat(e.slug))),history.replaceState({},"",i)},filterViewType:function(t){var e=this;return t.filter((function(t){return-1!=e.viewType.indexOf(t.type)}))},setViewType:function(t){t.length?this.viewType=t:this.viewType=["creative","group"],this.active.category&&this.loadEntities(this.active.category),this.active.entities&&!this.active.entities.length&&(this.active.category=null),this.getCount(this.active.sector)||(this.active.sector=null),this.active.search&&this.loadSearch(),this.active.favorites&&(this.active.entities=this.filterViewType(this.favorites)),this.computeGridSizes()},getCount:function(t){return t?this.viewType.reduce((function(e,i){return e+(t.stats?t.stats[i].count:0)}),0):0}},watch:{$mq:function(){this.computeGridSizes()}}},J=U,Z=(i("5f9a"),Object(d["a"])(J,a,n,!1,null,null,null)),Y=Z.exports,K=i("f13c"),W=i.n(K),Q=i("cc37");i("ff21"),i("e699");s["a"].use(W.a),s["a"].config.productionTip=!1,s["a"].prototype.$loading=!1,window.addEventListener("DOMContentLoaded",(function(){var t=document.querySelector("#language_switch input[name=language]").value;Q["a"].locale=t})),new s["a"]({i18n:Q["a"],render:function(t){return t(Y)}}).$mount("#app")},c214:function(t,e,i){},cb73:function(t,e,i){},cc37:function(t,e,i){"use strict";var s=i("a026"),a=i("a925");s["a"].use(a["a"]);var n={en:{index:{fav:"Favorites",search:"Search",delete_filters:"delete all filters",all:"All",fav_add:"Add to",fav_remove:"Remove from",fav_error:"You must be logged in to add favorites.",sector:"Sector",category:"Category",interests:"Interests",results:"result(s)",creative_profile:"Creative profile",group_profile:"Group profile",member_of:"Member of",members:"Members",view:"View",creatives:"Creatives",groups:"Groups",sort:{label:"Sort by",atoz:"A to Z",ztoa:"Z to A",numasc:"Count - ascending",numdesc:"Count - descending"}},mapping:{title:"Select up to 5 categories from any of the 11 sectors",confirm:"Confirm the selection",suggestText:"Can't find your place?",suggestLink:"Suggest a new category",empty:"\n        <p>Start by exploring the sectors from the left column. Each of the 11 sectors has a number of categories. Please select at least one and up to 5 categories, regardless of the sectors (you can choose all 5 categories from a single sector or from multiple sectors).</p>\n        <p>Please suggest Other categories, if you consider that some of them are missing or if the ones listed are not appropriated. The list of categories can grow and be more relevant through your input. The new suggestions will not appear only after they will be moderated by the Admins of this platform.</p>\n        <p>Please note that even after confirming the selection of the categories, you can still arrange them in order.</p>\n      ",info:"You can reorder the categories after adding them by drag & drop"},groups:{messages:{group_deleting:"Delete group",group_delete:"Are you sure you want to delete the group? <br/><b>This operation is permanent.</b>",group_deleted:"Group has been deleted",member_deleting:"Remove member",member_delete:"Are you sure you want to remove this member from the group?",member_deleted:"The member has been removed from the group"},add_member:"Add member",add_member_outside:"Add member from outside Creativa",pending:"Pending",invite:"Invite",invite_to:"Re-send invitation",invite_description:"We will send an e-mail invitation to join Creativa and once the user creates their profile, they will be added automatically",name:"Name",edit:"Edit",email:"E-mail address",role:"Member role",permissions:"Group permissions",save:"Save changes",cancel:"Cancel",roles:{admin:"Admin (can edit)",member:"Member"},manage:{search_empty:"No results",search:'Search "Creativa"',manage:"Manage",leave:"Leave group",left_group:"You have left the group",invitation_pending:"Pending invitations",invitation_accept:"Accept",invitation_decline:"Refuse",invitation_accepted:"Invitation accepted",invitation_declined:"Invitation declined",new_group:"+ Create a group",member_groups:"My groups",admin_groups:"Groups I manage",remove:"Remove member"}},login:"Login",or:"or"},ro:{index:{fav:"Favorite",search:"Căutare",delete_filters:"șterge toate filtrele",all:"Toate",fav_add:"Adaugă la",fav_remove:"Elimină de la",fav_error:"Trebuie să fii autentificat ca să adaugi favorite",sector:"Sector",category:"Categorie",interests:"Interese",results:"rezultat(e)",creative_profile:"Profil creativ",group_profile:"Profil grup",member_of:"Membru în",members:"Membrii",view:"Vezi",creatives:"Creativi",groups:"Grupuri",sort:{label:"Ordonează după",atoz:"A la Z",ztoa:"Z la A",numasc:"Număr - crescător",numdesc:"Număr - descrescător"}},mapping:{title:"Selectează una sau mai multe categorii",confirm:"Confirmă selecția",suggestText:"Nu-ți găsești locul?",suggestLink:"Sugerează o categorie nouă",empty:"\n        <p>Începe prin a explora sectoarele din coloana stângă. Fiecare dintre cele 11 sectoare are un număr de categorii. Vă rugăm să selectați cel puțin una și până la 5 categorii, indiferent de sectoare (puteți alege toate cele 5 categorii dintr-un singur sector sau din mai multe).</p>\n        <p>Te rugăm sa sugerezi alte noi categorii, dacă consideri că unele dintre ele lipsesc sau dacă cele enumerate nu sunt potrivite. Lista categoriilor poate crește și deveni mai relevantă și prin aportul tău. Noile categorii sugerate vor apărea doar după ce au fost moderate de către administratorii acestei platforme.</p>\n        <p>Te rugăm să reții că și după ce ai confirmat selecția de categorii, ai posibilitatea de a le aranja în ordine.</p>\n      ",info:"Poți repoziționa categoriile în ordinea importanței prin drag & drop"},groups:{messages:{group_deleting:"Ștergere grup",group_delete:"Ești sigur că vrei să ștergi grupul?  <br/><b>Această operațiune este ireversibilă.</b>",group_deleted:"Grupul a fost șters",member_deleting:"Eliminare membru",member_delete:"Ești sigur că vrei să elimini membrul din grup?",member_deleted:"Membrul a fost eliminat din grup"},add_member:"Adaugă membru",add_member_outside:"Adaugă membru din afara platformei",pending:"În așteptare",invite:"Invită",invite_to:"Trimite invitație din nou",invite_description:"Vom trimite o invitație pe e-mail și odată ce utilizatorul își completează profilul va fi adăugat automat",name:"Nume",edit:"Editează",email:"Adresă de e-mail",role:"Rolul membrului",permissions:"Permisiuni de grup",save:"Salvează modificări",cancel:"Anulează",roles:{admin:"Admin (poate edita)",member:"Membru"},manage:{search_empty:"Nu sunt rezultate",search:'Caută în "Creativa"',manage:"Administrează",leave:"Părăsește grupul",left_group:"Ai părăsit grupul",invitation_pending:"Invitații în așteptare",invitation_accept:"Acceptă",invitation_decline:"Refuză",invitation_accepted:"Invitație acceptată",invitation_declined:"Invitație respinsă",new_group:"+ Crează un grup",member_groups:"Grupuri din care fac parte",admin_groups:"Grupuri pe care le administrez",remove:"Elimină din grup"}},login:"Autentificare",or:"sau"}};e["a"]=new a["a"]({locale:"ro",fallbackLocale:"en",messages:n})},d7c2:function(t,e,i){"use strict";i.d(e,"b",(function(){return s})),i.d(e,"a",(function(){return a}));i("99af"),i("a15b"),i("d3b7");function s(t,e,i){var s=i?t:"/".concat(window.APP.lang?window.APP.lang:"ro","/api/").concat(t);return fetch(s,e).then((function(t){return 204==t.status?Promise.resolve():t.json().then((function(e){return t.ok?e:Promise.reject(JSON.stringify(e.non_field_errors.join("<br />")))}))}))}function a(t,e){var i=null;return function(){clearTimeout(i);var s=arguments,a=this;i=setTimeout((function(){t.apply(a,s)}),e)}}},e699:function(t,e,i){"use strict";var s=i("a026"),a=i("77b4"),n=i("ff69"),o=i("39ea"),r=i("10bd"),c=i("c0ac"),l=i("7f82"),u=i("7584"),d=i("61b7"),v=i("8cbf"),f=i("544d"),h=i("b897"),p=i("2c4e"),m=i("80f1"),g=i("f723"),y=i("aced"),b=i("d410"),_=i("f7da"),C=i("289d");s["a"].use(a["a"]),s["a"].use(n["a"]),s["a"].use(o["a"]),s["a"].use(r["a"]),s["a"].use(c["a"]),s["a"].use(l["a"]),s["a"].use(u["a"]),s["a"].use(d["a"]),s["a"].use(v["a"]),s["a"].use(f["a"]),s["a"].use(h["a"]),s["a"].use(p["a"]),s["a"].use(m["a"]),s["a"].use(g["a"]),s["a"].use(y["a"]),s["a"].use(b["a"]),s["a"].use(_["a"]),C["a"].setOptions({defaultTrapFocus:!0,defaultUseHtml5Validation:!1,defaultIconPack:"ionicons",customIconPacks:{ionicons:{iconPrefix:"ion-md-",internalIcons:{check:"checkmark","check-circle":"checkmark-circle-outline","alert-circle":"alert","chevron-right":"arrow-forward","chevron-left":"arrow-back","chevron-down":"arrow-down","menu-down":"arrow-dropdown","menu-up":"arrow-dropup"}}}})},f671:function(t,e,i){},f9e8:function(t,e,i){"use strict";i("4412")},ff21:function(t,e,i){"use strict";var s=i("a026"),a=i("660e");s["a"].use(a["a"],{breakpoints:{sm:769,md:1080,lg:1440,xl:1/0}})}});