from datetime import date

from django.shortcuts import get_object_or_404, redirect, render

from .models import Task


def task_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        due_date = request.POST.get("due_date")

        if title:
            Task.objects.create(
                title=title,
                due_date=due_date if due_date else None,
            )
        return redirect("task_list")

    search_query = request.GET.get("search", "")

    pending_tasks = Task.objects.filter(
        completed=False,
        title__icontains=search_query,
    ).order_by("due_date", "-created_at")

    completed_tasks = Task.objects.filter(
        completed=True,
        title__icontains=search_query,
    ).order_by("due_date", "-created_at")

    return render(
        request,
        "home.html",
        {
            "pending_tasks": pending_tasks,
            "completed_tasks": completed_tasks,
            "pending_count": pending_tasks.count(),
            "completed_count": completed_tasks.count(),
            "today": date.today(),
        },
    )


def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = True
    task.save()
    return redirect("task_list")


def undo_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = False
    task.save()
    return redirect("task_list")


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect("task_list")


def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == "POST":
        new_title = request.POST.get("title")
        new_due_date = request.POST.get("due_date")

        if new_title:
            task.title = new_title
            task.due_date = new_due_date if new_due_date else None
            task.save()

        return redirect("task_list")

    return render(request, "edit_task.html", {"task": task})
