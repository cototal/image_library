import $ from "jquery";
import "bootstrap";

import '../css/app.scss';

$(() => {
    const existingTagContainer = $("#existing-tag-container");
    const tagInput = $("#tag");
    if (existingTagContainer.length > 0) {
        const readyTags = async () => {
            const tagResp = await $.get("/tag-list");

            tagInput.on("input", evt => {
                const val = evt.target.value;
                if (val.length < 2) {
                    existingTagContainer.html('');
                    return;
                }
                const matches = tagResp.names.filter(n => n.includes(val));
                existingTagContainer.html(`<ul class="list-inline">${matches.map(m => `<li class="list-inline-item existing-tag">
                    <button role="button" type="button" class='btn btn-outline-dark btn-sm'>${m}</button>
                </li>`).join('')}</ul>`);
            })
        };
        readyTags();
    }
    $(document).on("click", ".existing-tag", evt => {
        tagInput.val($(evt.target).text());
    });
    $("#selectAllImages").on("click", () => {
        $(".image-checkbox").attr("checked", true);
    });
    $("#deselectAllImages").on("click", () => {
        $(".image-checkbox").attr("checked", false);
    });
    $(".tag-name").on("click", evt => {
        tagInput.val($(evt.target).text());
    });
    $(".apply-tag-button").on("click", async evt => {
        const action = $(evt.target).data("action");
        const checkedImageIds = [];

        $(".image-checkbox:checked").each((idx, el) => {
            checkedImageIds.push(el.value);
        });

        const token = $("input[name='csrfmiddlewaretoken']").val();
        const tagName = tagInput.val();

        try {
            const resp = await $.ajax({
                url: "/tags/add-remove",
                type: "POST",
                dataType: "JSON",
                contentType: "application/json",
                data: JSON.stringify({ action, ids: checkedImageIds, name: tagName }),
                headers: {
                    "X-CSRFToken": token
                }
            });
            window.location.href = window.location.href;
        } catch (err) {
            console.error(err);
        }
    });
})();
